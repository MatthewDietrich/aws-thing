from requests import get

PREV_IP_FILE_PATH = ".public_ip.txt"
DEFAULT_IP = "127.0.0.1"

def get_public_ip():
    """Retrieve this machine's public IP address from an API"""
    public_ip = get('https://api.ipify.org').text
    return public_ip

def get_previous_ip():
    """Look up previous IP in locally stored file. If the file does not exist, create it"""
    prevFile = ""
    retval = ""
    try:
        prevFile = open(PREV_IP_FILE_PATH, 'r')
        prevFile.close()
    except IOError:
        set_previous_ip(DEFAULT_IP)
    finally:
        prevFile = open(PREV_IP_FILE_PATH, 'r')
        retval = prevFile.readlines()[0]
        prevFile.close()
    return retval

def set_previous_ip(ip):
    """Replace contents of previous public IP file"""
    prevFile = open(PREV_IP_FILE_PATH, 'w')
    prevFile.write(ip)
    prevFile.close()

if __name__ == "__main__":
    print ("Finding previous public IP")
    previous_ip = get_previous_ip()
    print (previous_ip)
    print ("Retrieving public IP")
    public_ip = get_public_ip()
    print (public_ip)

    if (public_ip != previous_ip):
        print ("IP has changed. Storing new IP.")
        set_previous_ip(public_ip)

    else:
        print ("IP has not changed.")
