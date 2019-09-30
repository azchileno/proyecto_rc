# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
      _name='proyecto_rc.libro'
      _rec_name='nombre_cuenta'
     
      fecha = fields.Date(string="Fecha")
      nombre_cuenta=fields.Char(string="Nombre cuenta")
      debe=fields.Float(string="Debe")
      haber=fields.Float(string="Haber")
      total=fields.Float(string="Total")

      detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='libro_id', string='Libro', 
          required=True)

class Detalle_libro(models.Model):
      _name='proyecto_rc.detalle_libro'
      _rec_name='fecha'
     
      fecha=fields.Date(string="Fecha")
      descripcion=fields.Text(string="Descripción")    
      cantidad_debe=fields.Float(string="Cantidad debe")
      cantidad_haber=fields.Float(string="Cantidad haber")  
      total_debe=fields.Float(string="Debe")
      total_haber=fields.Float(string="Haber")

      libro_id = fields.Many2one(comodel_name='proyecto_rc.libro', string='Libro')
      producto_id = fields.Many2one(comodel_name='proyecto_rc.producto', string='Producto')   
      movimiento_id = fields.Many2one(comodel_name='proyecto_rc.movimiento', string='Movimiento')   
      cuenta_id = fields.Many2one(comodel_name='proyecto_rc.cuenta', string='Cuenta')      
      empresa_id = fields.Many2one(comodel_name='proyecto_rc.empresa', string='Empresa')      
      factura_id = fields.Many2one(comodel_name='proyecto_rc.factura', string='Factura')      

class Producto(models.Model):
      _name = 'proyecto_rc.producto'
      _rec_name = 'nombre'
 
      nombre = fields.Char(string="Nombre", required=True)
      categoria=fields.Selection([('lubricante','Lubricante'),('accesorios','Accesorios'),('motor','Motor')],string="Categoria", required=True) 
      marca = fields.Char(string="Marca", required=True)
      modelo = fields.Char(string="Modelo", required=True)
      cantidad_disponible=fields.Float(string="Cantidad disponible", required=True)  
      precio_compra = fields.Char(string="Precio compra", required=True)
      precio_venta = fields.Char(string="Precio venta", required=True)
      descripcion=fields.Text(string="Descripción")

      detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='producto_id', string='Tipo movimiento', 
          required=True)
      
class Empresa(models.Model):
      _name='proyecto_rc.empresa'
      _rec_name='nombre'
     
      nombre = fields.Char(string="Nombre", required=True)
      rut = fields.Char(string="Rut", required=True)
      direccion = fields.Char(string="Dirección", required=True)
      telefono = fields.Char(string="Teléfono", required=True)
      correo = fields.Char(string="Correo", required=True)

      detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='empresa_id', string='Libro', 
          required=True)

class Factura_venta(models.Model):
      _name='proyecto_rc.factura_venta'
      _rec_name='fecha'
     
      fecha = fields.Date(string="Fecha", required=True)
      tipo_pago=fields.Selection([('efectivo','Efectivo'),('Debito','debito')],string="Tipo de pago", required=True) 
      total_factura_venta=fields.Float(string="Total", required=True)
      trabajador_id = fields.Many2one(comodel_name='proyecto_rc.trabajador', string='Vendedor')

      detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='factura_id', string='Libro', 
          required=True)
      #tipo_empresa_id = fields.Many2one(comodel_name='proyecto_rc.tipo_empresa', string='Tipo empresa')
      trabajador_id = fields.Many2one(comodel_name='proyecto_rc.trabajador', string="Trabajador")

class Factura_compra(models.Model):
       _name='proyecto_rc.factura_compra'
       _rec_name='fecha'
     
       fecha = fields.Date(string="Fecha", required=True)
       total_factura_compra=fields.Float(string="Total", required=True)
       trabajador_id = fields.Many2one(comodel_name='proyecto_rc.trabajador', string='Vendedor')

       detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='factura_id', string='libro', 
           required=True)
      #tipo_empresa_id = fields.Many2one(comodel_name='proyecto_rc.tipo_empresa', string='Tipo empresa')
       trabajador_id = fields.Many2one(comodel_name='proyecto_rc.trabajador', string="Trabajador")

#class Categoría (models.Model):
      #_name='proyecto_rc.categoria'
      #_rec_name='categoria'
     
      #categoria = fields.Char(string="Categoría", required=True)
      #descripcion=fields.Text(string="Descripción")

      #producto_ids=fields.One2many(comodel_name='proyecto_rc.producto', inverse_name='categoria_id', string='Producto', 
        #required=True)

class Cuenta(models.Model):
      _name='proyecto_rc.cuenta'
      _rec_name='titulo'
 
      titulo=fields.Char(string="Nombre")
      tipo_cuenta=fields.Selection([('a pagar','A pagar'),('a cobrar','A cobrar'),('banco y caja','Banco y caja')],string="Tipo de movimiento", required=True) 

      detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='cuenta_id', string='Detalle libro',required=True)

class movimiento(models.Model):
      _name='proyecto_rc.movimiento'
      _rec_name='movimiento'
     
      movimiento=fields.Selection([('compra','Compra'),('venta','Venta'),('merma','Merma')],string="Tipo de movimiento", required=True) 
      descripcion=fields.Text(string="Descripción")
      total_movimiento=fields.Float(string="Total movimiento", required=True)

      detalle_libro_ids=fields.One2many(comodel_name='proyecto_rc.detalle_libro', inverse_name='movimiento_id', string='Libro', 
          required=True)


class Trabajador(models.Model):
      _name = 'proyecto_rc.trabajador'
      _rec_name = 'nombre'
 
      nombre = fields.Char(string="Nombre", required=True)
      rut = fields.Char(string="Rut", required=True)
      sexo=fields.Selection([('femenino','Femenino'),('masculino','Masculino')],string="sexo",required=True)
      direccion = fields.Char(string="Dirección", required=True)
      telefono = fields.Char(string="Teléfono (+56)", size=9, required=True)
      cargo=fields.Selection([('vendedor','Vendedor'),('cajero','Cajero')],string="Cargo", required=True)

      factura_venta_ids=fields.One2many(comodel_name='proyecto_rc.factura_venta', inverse_name='trabajador_id', string='Factura venta', 
           required=True)
      factura_compra_ids=fields.One2many(comodel_name='proyecto_rc.factura_compra', inverse_name='trabajador_id', string='Factura compra', 
           required=True)

# class proyecto_rc(models.Model):
#     _name = 'proyecto_rc.proyecto_rc'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100