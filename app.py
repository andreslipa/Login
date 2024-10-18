from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_123'  # Clave secreta para manejar la sesión

# Información de usuario de ejemplo
users = {
    "andres": "12345",
    "usuario2": "contraseña2"
}

@app.route('/')
def home():
    # Si el usuario está autenticado, redirigir a la página de bienvenida
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar si el usuario existe y si la contraseña es correcta
        if username in users and users[username] == password:
            session['username'] = username  # Almacenar el nombre de usuario en la sesión
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    # Solo permitir acceso si el usuario está autenticado
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar la información de sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
