import os
import copy

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

db.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER, user_id NUMERIC NOT NULL, symbol TEXT NOT NULL, companyname TEXT NOT NULL, \
            shares NUMERIC NOT NULL, price NUMERIC NOT NULL, transType TEXT NOT NULL, timestamp TEXT DEFAULT current_timestamp, PRIMARY KEY(id), \
            FOREIGN KEY(user_id) REFERENCES users(id))")
db.execute("CREATE INDEX IF NOT EXISTS orders_by_user_id_index ON orders (user_id)")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
 # Get all orders by the user (user obtained by checking the session)if request.method == "POST":
    if request.method == "POST":
        user = session["user_id"]
        data = db.execute("SELECT *, \
                        sum(CASE WHEN transType = 'bought' THEN shares END) - \
                        sum(CASE WHEN transType = 'sold' THEN shares ELSE 0 END) AS totalshares \
                        FROM orders WHERE user_id = ? \
                        GROUP BY symbol", user)
        cash = db.execute("SELECT cash FROM users WHERE id = (?)", user)[
            0]["cash"]

        shares = []
        if 'buy' in request.form:
            for data in data:
                symbol = data["symbol"]
                if request.form.get(f"shares{symbol}"):
                    shares = int(request.form.get(f"shares{symbol}"))
                    shareprice = float(data["price"]) * shares
                    if cash < shareprice:
                        foo = "too poor"
                        return apology("you are poor", 403)
                    else:
                        foo = "rich man"
                        # Insert the purchase into the orders table
                        db.execute("INSERT INTO orders (user_id, symbol, companyname, shares, price, transType) \
                                    VALUES (?, ?, ?, ?, ?, ?)", user, symbol, data["companyname"], shares, data["price"], "bought")
                        # Update the amount of cash the user has now
                        db.execute(
                            "UPDATE users SET cash = cash - ? WHERE id = ?", shareprice, user)
                        return redirect("/")
                else:
                    continue
        return redirect("/")

    else:
        user = session["user_id"]
        data = db.execute("SELECT *, \
                        sum(CASE WHEN transType = 'bought' THEN shares END) - \
                        sum(CASE WHEN transType = 'sold' THEN shares ELSE 0 END) AS totalshares \
                        FROM orders WHERE user_id = ? \
                        GROUP BY symbol", user)

        cash = db.execute("SELECT cash FROM users WHERE id = (?)", user)[
            0]["cash"]

        for i in range(0, len(data)):
            if data[i]["totalshares"] < 1:
                data[i] = 0

        rowCash = []
        for i in range(len(db.execute("SELECT symbol FROM orders  WHERE user_id = ? GROUP BY symbol", user))):
            if data[i] != 0:
                current = lookup(data[i]["symbol"])
                rowCash.append((current["price"]*data[i]["totalshares"]))

        totalCash = 0
        for i in range(len(rowCash)):
            totalCash += rowCash[i]
        totalCash += cash
        return render_template("index.html", data=data, cash=cash, totalCash=totalCash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # Post method used for sending the form. So basically this is only if you filled the form and clicked submit
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide a symbol", 400)

        try:


                                        
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("only numbers you cheeky bastard", 400)
         # Ensure number of shares was submitted
        if not shares or shares < 1:
            return apology("must provide a valid number", 400)
        # If everything correct, get the symbol and call the API with it
        data = lookup(request.form.get("symbol"))
        # If the reply is empty (symbol not valid)
        if data == None:
            return apology("must provide a valid symbol", 400)
        # If the symbol is correct
        else:
            user = session["user_id"]
            multp = int(request.form.get("shares"))
            companyName = data["name"]
            companySymbol = request.form.get("symbol").upper()
            moolah = float(data["price"])

            # Calculate the total
            total = moolah * multp

            # Get the cash the user has
            cash = db.execute("SELECT cash FROM users WHERE id = (?)", session["user_id"])[
                0]["cash"]

            if total <= cash:
                bought = multp
                newCash = (cash - total)
            # If the user doesn't have enough money
            else:
                return apology("You are poor.", 403)
            # Insert the purchase into the orders table
            db.execute("INSERT INTO orders (user_id, symbol, companyname, shares, price, transType) \
                        VALUES (?, ?, ?, ?, ?, ?)", user, companySymbol, companyName, bought, moolah, "bought")
            # Update the amount of cash the user has now
            db.execute("UPDATE users SET cash = ? WHERE id = ?", newCash, user)
            return redirect("/")

        # If the user gets to this page via get (as in clicking a link of typing the address)
    else:
        # Query the databes and get the users cash (maybe unnecesary, I'll have to check if i'm actually using it)
        cash = db.execute(
            "SELECT cash FROM users WHERE id = (?)", session["user_id"])
        return render_template("buy.html", cash=cash)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Get all the transactions the user has done
    histories = db.execute(
        "SELECT * FROM orders WHERE user_id = (?)", session["user_id"])
    # Render the history pape and pass the data to be used by the template
    return render_template("history.html", histories=histories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # If the user submits the form
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide a symbol", 400)
        # Use the API to get the data corresponding to that symbol
        data = lookup(request.form.get("symbol"))
        # If the API returns nothing, the symbol is not valid
        if lookup(request.form.get("symbol")) == None:
            return apology("must provide a valid symbol", 400)
         # If the request to the API is successfull
        else:
            # Render the quoted page and pass the data to the template
            return render_template("quoted.html", data=data)
    # If the user lands on this page by typing the address or clicking a link
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by clicking submit)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide an username", 400)

         # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide a password", 400)

         # Ensure password and confirmation match
        if (request.form.get("password") != request.form.get("confirmation")):
            return apology("passwords must match", 400)

        if (request.form.get("password") == request.form.get("confirmation")):
            newPassword = request.form.get("password")
            user = request.form.get("username")

            userCheck = db.execute("SELECT username FROM users")
            for i in range(0, len(userCheck)):
                if (request.form.get("username") == userCheck[i]["username"]):
                    return apology("that username already exists", 400)
        # Hash password
        hash = generate_password_hash(newPassword)

        # Insert into the users table the user and hash password.
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", user, hash)
        return redirect("/")

    # User reached route via GET (as by clicking a link)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide a symbol", 400)

         # Ensure number of shares was submitted
        if not request.form.get("shares"):
            return apology("must provide a number of shares", 400)
        # Get all the shares owned by the user
        user = session["user_id"]
        owned = db.execute("SELECT *, \
                    sum(CASE WHEN transType = 'bought' THEN shares END) - \
                    sum(CASE WHEN transType = 'sold' THEN shares ELSE 0 END) AS totalshares \
                    FROM orders WHERE user_id = ? \
                    GROUP BY symbol", user)

        for i in range(0, len(owned)):
            if owned[i]["totalshares"] < 1:
                owned[i] = 0

        total = 0
        totalShares = 0
        # Loop though all the entries and select the one that matches the symbol requested by the user
        for owned in owned:
            if owned != 0:
                if request.form.get("symbol").upper() == owned["symbol"]:
                    # Get the data from the API by querying the symbol in the form
                    data = lookup(request.form.get("symbol"))
                    # Get the price per share from the data and convert into float
                    price = float(data["price"])
                    # Get the multiplier from the form filled by the user and turn into int
                    multp = int(request.form.get("shares"))
                    # Calcualte the total
                    total = (price * multp)

        if int(request.form.get("shares")) > owned["totalshares"]:
            return apology("You dont have enough shares", 400)

        else:
            db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",
                       total, session["user_id"])
            db.execute("INSERT INTO orders (user_id, symbol, companyname, shares, price, transType) \
                            VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], data["symbol"], data["name"], multp, data["price"], "sold")
        return redirect("/")

    else:
        symbols = db.execute("SELECT *, sum(CASE WHEN transType = 'bought' THEN shares END) - \
        sum(CASE WHEN transType = 'sold' THEN shares ELSE 0 END) AS totalshares FROM orders WHERE user_id = ? GROUP BY symbol", session["user_id"])
        return render_template("sell.html", symbols=symbols)
