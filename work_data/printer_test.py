import json, os, random, datetime
from printer import Receipt
from escpos import printer

eps = printer.Usb(0x4b8,0x0e03)
curdir = os.path.dirname(os.path.abspath(__file__))
jsnf = os.path.join(curdir,'items.json')
jsn = open(jsnf)
items = json.load(jsn)
receipt = Receipt()
rno = str(random.randint(10000,1000000))
opts = {
    'cname':'MANGO & PEAR ENTERPRISE LTD DEALERS IN FRUITS',
    'clogo':'uploads/clogo.png',
    'cinfo':'+2631111111 / +263111111',
    'cloc':'',
    'rname':'Sales Receipt',
    'rno':rno,
    'customer':'',
    'cashier':'ME AM ME',
    'currency':'',
    'rdate':datetime.datetime.today().ctime(),
}
receipt.print_header(opts)
receipt.print_items(items)
receipt.print_message('THANKS FOR YOUR PATRONAGE')
receipt.print_vat('Amount is VAT INCLUSIVE')
receipt.print_me('Programmed by : Softwares . : +26311111')
# eps.text(receipt._receipt)
# eps.cut()
receipts_dir = os.path.join(curdir,'receipts')
if not os.path.exists(receipts_dir):
    os.mkdir(receipts_dir)

receipt_name = 'r'+rno+'.txt'
with open(os.path.join(receipts_dir,receipt_name),'w') as rcpt:
    rcpt.write(receipt._receipt)
