import openai
import os

# input = image, dict of data
# want to create title, description, and image variations

class ChatGPT():
    def __init__(self):
        openai.api_key = os.getenv("openaikey")
    
    @staticmethod
    def generatePostInfo(typeOfProduct,formData, fileUrl):
        brand = formData["brand"]
        condition = formData["condition"]
        images = ChatGPT.__imgRequest(fileUrl)
        size = ""
        title = ""
        desc = ""

        if typeOfProduct == "laptop":
            size = formData["screen_size"]
            title = ChatGPT.__titleRequest(brand, condition, "laptop", size)
            desc = ChatGPT.__descRequest(brand, condition, "laptop", size)
            
        
        elif typeOfProduct == "desktop":
            title = ChatGPT.__titleRequest(brand, condition, "desktop")
            desc = ChatGPT.__descRequest(brand, condition, "desktop")

        elif typeOfProduct == "camera":
            title = ChatGPT.__titleRequest(brand, condition, "camera")
            desc = ChatGPT.__descRequest(brand, condition, "camera")

        returnDic = {
            "type": typeOfProduct,
            "brand": brand,
            "condition": condition,
            "title": title,
            "description": desc,
            "images": images,
        }
        if typeOfProduct == "laptop":
            returnDic["size"] = size
        
        return returnDic

    @staticmethod
    def __titleRequest(brand,condition, deviceType, size=""):
        req = f"I'm selling a {brand} {size} {deviceType} whose condition is {condition}. Please generate a title for a craigslist post for this item. You are allowed to answer only in one line which is the title"

        response = openai.Completion.create(model="text-davinci-003", prompt=req, temperature=0, max_tokens=4000)
        return response["choices"][0]["text"].replace("\"","").replace(".","")

    @staticmethod
    def __descRequest(brand, condition, deviceType, size=""):
        req = f"I'm selling a {brand} {size} {deviceType} whose condition is {condition}. Please generate a 100 word description for a craigslist post for this item. You are only allowed to reply with the description, nothing else."

        response = openai.Completion.create(model="text-davinci-003", prompt=req, temperature=0, max_tokens=4000)
        return response["choices"][0]["text"].replace("\"","").replace(".","")
    
    @staticmethod
    def __imgRequest(fileUrl):
        images = []
        with open(fileUrl, "rb") as image:
            response = openai.Image.create_variation(
                image,
                n=5,
                size="1024x1024"
            )
            response = response["data"]
            for img in response:
                images.append(img["url"])
        return images
