


from parser_engines.parser_factory import ParserManager

if __name__ == "__main__":

  # TEST_URL = "https://www.techradar.com/phones/samsung-galaxy-phones/new-dummy-unit-leak-may-have-revealed-exactly-how-thin-the-galaxy-z-fold-7-is-going-to-be"
  TEST_URL = "https://techcrunch.com/2025/06/19/spacexs-starship-blows-up-ahead-of-10th-test-flight/"

  # Calling manager to get the correct parser base on the domain
  manager = ParserManager()
  # parser = manager.get_parser("https://techcrunch.com/2025/06/19/spacexs-starship-blows-up-ahead-of-10th-test-flight/")
  parser = manager.get_parser(TEST_URL)


  """ There is 2 ways to do parse a page """

  # Approach 1: Setting url using parser.url and calling parse() to get a result
  """parser.url = TEST_URL

  content = parser.parse() """

  # Approach 2: Calling parse() and passing the url at the same time as it was built in with the function
  content = parser.parse(TEST_URL)

  print(content)