
import anvil.server

anvil.server.connect("O6HUI7ZPHPGAUYQSLUMJSCO3-5ESUVNCA6HH7DJWQ")

@anvil.server.callable
def say_hello(name):
  print(f"Hello from your own machine, {name}!")

anvil.server.wait_forever()