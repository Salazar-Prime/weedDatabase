import streamlit as st
import streamlit.components.v1 as components
import yaml
from yaml.loader import SafeLoader
import seaborn as sns


sns.set_theme(style="darkgrid")
sns.set()

# USER Imports
from authentication import Authenticate, Hasher
import tabbed
from utils import getWeedList

_RELEASE = False


def startApp():
    st.title("SURF Template Generator")
    weedList = getWeedList("src/config/weedClassList.txt")
    tabs = tabbed.start_tabs(weedList)


def main():
    if _RELEASE:

        ######### Login System for the Dashboard ################

        # Loading authentication config file
        with open("config.yaml") as file:
            config = yaml.load(file, Loader=SafeLoader)

        # Creating the authenticator object
        authenticator = Authenticate(
            config["credentials"],
            config["cookie"]["name"],
            config["cookie"]["key"],
            config["cookie"]["expiry_days"],
            config["preauthorized"],
        )

        # create login UI
        name, authentication_status, username = authenticator.login("Login", "main")

        # condition access to the app with the authentication status
        if st.session_state["authentication_status"]:
            authenticator.logout("Logoff", "sidebar")
            with st.sidebar:
                st.write(f'Welcome *{st.session_state["name"]}*')
            startApp()
        elif st.session_state["authentication_status"] == False:
            st.error("Username/password is incorrect")
    else:
        startApp()


if __name__ == "__main__":
    main()
