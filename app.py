import streamlit as st

# Initialization

if 'session' not in st.session_state:
    st.session_state['session'] = False


if st.session_state["session"] == True:
    st.title("Bienvenido 🎉")
else:
    st.title("🔐 Inicio de Sesión")

    # Solicitar credenciales
    user = st.text_input("Usuario:")
    password = st.text_input("Contraseña", type="password")
 
    
    if st.button("Iniciar Sesión"):
        if user == st.secrets.session.user and int(password) == st.secrets.session.password:
                st.session_state["session"] = True
                st.success("✅ Usuario y contraseña correctos ✅")
                st.rerun()
        else:
            st.session_state = False
            st.error("❌ Usuario o contraseña incorrectos. ❌")

