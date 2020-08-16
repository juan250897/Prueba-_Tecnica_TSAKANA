import os
from flask import Flask,redirect,url_for, render_template,request,flash
from datetime import datetime
from flask_mysqldb import MySQL




app= Flask(__name__)

app.secret_key ='clave_secreta_flask'

#context procesor
@app.context_processor
def date_now():
    return{
        'now':datetime.utcnow()
    }
#endpoints

#conexion DB
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] = 'prueba_tecnica_tsakana'



mysql = MySQL(app)

@app.route('/')



#para registar

def index():
    return render_template('index.html')

@app.route('/registrar-productos', methods=['GET','POST'])
def registrar_productos ():

    if request.method == 'POST':

        categoria = request.form['categoria']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        estado = request.form['estado']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO productos VALUES(NULL,%s,%s,%s,%s,%s)",(categoria, nombre, precio, cantidad, estado))
        cursor.connection.commit()

        flash('Has agregado el producto correctamente!!')

        return redirect(url_for('registrar_productos'))

    return render_template('registrar_producto.html')


@app.route('/registrar-clientes/',methods=['GET','POST'])
def registrar_clientes():
     if request.method == 'POST':

        cedula = request.form['cedula']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        
        

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO clientes VALUES(%s,%s,%s,%s)",(cedula, nombre, direccion, telefono))
        cursor.connection.commit()

        flash('Has agregado un cliente correctamente!!')

        return redirect(url_for('registrar_clientes'))

     return render_template('registrar_cliente.html')
             
@app.route('/registrar-facturas',methods=['GET','POST'])
def registrar_facturas ():

     if request.method == 'POST':

        cliente = request.form['cliente']
        productos = request.form['productos']
        cantidad = request.form['cantidad']
        fecha = request.form['fecha']
        total = request.form['total']
        metodo_pago = request.form['metodo_pago']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO facturas VALUES(NULL,%s,%s,%s,%s,%s,%s)",(cliente, productos, cantidad, fecha,total,metodo_pago))
        cursor.connection.commit()

        flash('Has agregado una factura correctamente!!')

        return redirect(url_for('registrar_facturas'))
    
     return render_template('registrar_factura.html')

#para ver listas

@app.route('/productos')
def productos():

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM productos")
     productos = cursor.fetchall()
     cursor.close()

     return render_template('productos.html', productos = productos)



@app.route('/clientes')
def clientes():

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM clientes")
     clientes = cursor.fetchall()
     cursor.close()

     return render_template('clientes.html', clientes = clientes)


@app.route('/facturas')
def facturas():

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM facturas")
     facturas = cursor.fetchall()
     cursor.close()

     return render_template('facturas.html', facturas = facturas)




#para borrar clientes

@app.route('/borrar-clientes/<int:cedula_id>')
def borrar_cliente(cedula_id):
     cursor = mysql.connection.cursor()
     cursor.execute(f"DELETE FROM clientes WHERE cedula= {cedula_id}")
     cursor.connection.commit()

     flash('Has borrado el cliente correctamente')

     return redirect (url_for('clientes'))

#para ver pagina de detalle

@app.route('/producto/<producto_id>')
def producto(producto_id):

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM productos WHERE codigo =%s",[producto_id])
     producto= cursor.fetchall()
     cursor.close()

     return render_template('producto.html', producto = producto[0])


@app.route('/cliente/<cedula_id>')
def cliente(cedula_id):

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM clientes WHERE cedula =%s",[cedula_id])
     cliente= cursor.fetchall()
     cursor.close()

     return render_template('cliente.html', cliente = cliente[0])


@app.route('/factura/<factura_id>')
def factura(factura_id):

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM facturas WHERE codigo =%s",[factura_id])
     factura= cursor.fetchall()
     cursor.close()

     return render_template('factura.html', factura = factura[0])


#para editar productos

@app.route('/editar-producto/<producto_id>', methods = ['GET','POST'])
def editar_producto(producto_id):


     if request.method == 'POST':

        categoria = request.form['categoria']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        estado = request.form['estado']

        cursor = mysql.connection.cursor()
        cursor.execute(""" 

            UPDATE productos 
            SET categoria = %s,
                nombre =%s, 
                precio = %s, 
                cantidad = %s, 
                estado =%s 
            WHERE codigo = %s 

        """,(categoria, nombre ,precio, cantidad, estado, producto_id))
        cursor.connection.commit()

        flash('Has editado el producto correctamente!!')


        return redirect(url_for('productos'))

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM productos WHERE codigo =%s",[producto_id])    
     producto= cursor.fetchall()
     cursor.close()

     return render_template('registrar_producto.html', producto = producto[0])



@app.route('/editar-cliente/<cedula_id>', methods = ['GET','POST'])
def editar_cliente(cedula_id):


     if request.method == 'POST':

       
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        

        cursor = mysql.connection.cursor()
        cursor.execute("""
        
            UPDATE clientes
            SET nombre = %s,
                direccion = %s,
                telefono =%s
            WHERE cedula = %s
        
        """,(nombre, direccion, telefono,cedula_id))
        cursor.connection.commit()

        flash('Has editado el cliente correctamente!!')


        return redirect(url_for('clientes'))

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM clientes WHERE cedula =%s",[cedula_id])    
     cliente= cursor.fetchall()
     cursor.close()

     return render_template('registrar_cliente.html', cliente = cliente[0])



@app.route('/editar-factura/<factura_id>', methods = ['GET','POST'])
def editar_factura(factura_id):


     if request.method == 'POST':

       
        cliente = request.form['cliente']
        productos = request.form['productos']
        cantidad = request.form['cantidad']
        fecha = request.form['fecha']
        total = request.form['total']
        metodo_pago = request.form['metodo_pago']
        

        cursor = mysql.connection.cursor()
        cursor.execute("""
        
            UPDATE facturas
            SET cliente = %s,
                productos = %s,
                cantidad =%s,
                fecha =%s,
                total =%s,
                metodo_pago =%s
            WHERE codigo = %s
        
        """,(cliente, productos, cantidad, fecha,total,metodo_pago,factura_id))
        cursor.connection.commit()

        flash('Has editado la factura correctamente!!')


        return redirect(url_for('facturas'))

     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM facturas WHERE codigo =%s",[factura_id])    
     factura= cursor.fetchall()
     cursor.close()

     return render_template('registrar_factura.html', factura = factura[0])



if __name__ == '__main__':
    app.run(debug=True)
    