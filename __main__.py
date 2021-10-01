from yattag import Doc
doc, tag, text = Doc().tagtext()        

import searchfile
#import callselenium
def main(args):
  with tag("html"):                     
    with tag("body"):
      with tag("h1"):
        text("search: %s" %
        searchfile.searchfile(args.get("url")))
#	  callselenium.callselenium(args.get("url")))
  return {
    "body": doc.getvalue()             
  }
