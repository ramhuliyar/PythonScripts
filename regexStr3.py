import re
string = '''
someOtherMessage{
              class = "someClass";
      sampleMessage{
                  someValue{
                      someText{
                          someParam = "value";
                          someSymbol = "another_symbol";
                      }; //someText
                  }; //someValue
       }; //sampleMessage
    }; //someOtherMessage
'''
pattern = re.compile(r'(\{.*\})',re.DOTALL)

match = re.search(pattern,string)
#print(match.group(1))

match = re.search(r"(\{.*\})", string,re.DOTALL)
print(match.group(1))
