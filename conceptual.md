### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Both languages are dynamically typed.  Python is well suited for back edn development thanks to a wide library of tools like Flask, while JavaScript is more commonly used in front end development as most web browsers are designed to work with the language.  Python's syntax is more simple and readable than JavaScript's.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?

  Testing if a single component of an application is working correctly

- What is an integration test?

  Testing if two or more components like functions or classes work together correctly

- What is the role of web application framework, like Flask?

  Server side web frameworks like Flask take most of the work out of handling HTTP requests for individual pages of a website, as well as handling how a site accesses data from a database.  

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    Path parameters are useful in retrieving information from a specified source, while query params are used for sorting or filtering results.

- How do you collect data from a URL placeholder parameter using Flask?

  Create a variable url by including a <name> in the url placeholder and accepting a corresponding name argument in the route's function.

- How do you collect data from the query string using Flask?

  Flask includes a 'request' object which allows for access of information relating to the currect HTTP request, including the url which contains the query string value.

- How do you collect data from the body of the request using Flask?

  request.get_json()?

- What is a cookie and what kinds of things are they commonly used for?

  Cookies are bits of data that are saved in a user's web browser for later use.

- What is the session object in Flask?

  Temporary data stored in a user's browser which is set to expire after a certain amount of time or after the user ceases to use the application.

- What does Flask's `jsonify()` do?

  Serializes data from python to JavaScript Object Notation
