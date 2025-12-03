from dotenv import load_dotenv

load_dotenv()
#
# def main():
#     print("Hello from pythonproject2!")

def get_text_length(text:str) -> int:
    """Returns the length of a text by characters"""
    return len(text)

if __name__ == "__main__":

    print(get_text_length(text='Dogesh'))
