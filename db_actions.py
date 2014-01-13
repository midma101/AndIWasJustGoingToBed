import sys

from sqlalchemy import create_engine 
from werkzeug.security import generate_password_hash, check_password_hash

from config import SQLALCHEMY_DATABASE_URI as engine_info


engine = create_engine(engine_info)
connection = engine.connect()

def usage():
    print("******************************************************")
    print ("Must add additional arguments when running the script")
    print("******************************************************")
    print ("")
    print ("delete_all           delete all posts")
    print ("load                 load an SQL dump")
    print ("add_user             add a user to the system")
    print("******************************************************")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
    elif sys.argv[1] == "delete_all":     
        result = connection.execute("delete from posts")
    elif sys.argv[1] == "add_user":  
        name = str(raw_input("Name?: "))
        password = str(raw_input("Password?: "))   
        query = ["insert into users (name, pw_hash) values ('",name,"','",password,"')"]
        result = connection.execute("".join(query))
        import pdb; pdb.set_trace()
    
