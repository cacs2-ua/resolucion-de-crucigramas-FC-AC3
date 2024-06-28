from main import *

def main():
    filename = 'tests/resources/Boards_Examples/d0.txt'
    result = create_storage_with_hash_table(filename)
    print(result)
    

if __name__=="__main__":
    main()