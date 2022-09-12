import json


class Valuefetch:
    def process(self, jsonInput, key):
        try:
            print("Input Object\t" + jsonInput)
            print("Input Key\t" + key)
            keyList = []
            if key.find("/") > 0:
                keyList = key.split("/")
            else:
                keyList = [key]
            jsonObj = json.loads(jsonInput)
            hasvalue = True
            for k in keyList:
                if k in jsonObj.keys():
                    jsonObj = jsonObj[k]
                else:
                    print("Invalid key " + k + "\n")
                    hasvalue = False
                    return "Invalid key:\t" + k
            if hasvalue:
                print("value :\t" + str(jsonObj) + "\n")
                return str(jsonObj)
        except ValueError:
            print("Invalid Json input " + "\n")
            return "Invalid Json input"
        except:
            print("Invalid input " + "\n")
            return "Invalid input"


if __name__ == '__main__':
    print("Input object json")
    jsonInput = input()
    print("Input key list to find value")
    keyList = input()

    valueFetch = Valuefetch()
    valueFetch.process(jsonInput, keyList)
