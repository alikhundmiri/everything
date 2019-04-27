response = unirest.post("https://yodish.p.rapidapi.com/yoda.json?text=Master+Obiwan+has+lost+a+planet.",
  headers={
    "X-RapidAPI-Host": "yodish.p.rapidapi.com",
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)