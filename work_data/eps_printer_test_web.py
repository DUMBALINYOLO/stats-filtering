import json, os, random, datetime
from work_data.eps_printer import Receipt

def dummy_print(items, opts):
    curdir = os.path.dirname(os.path.abspath(__file__))
    pic = 'tux.jpg'
    receipt = Receipt()
    clogo = 'uploads/'+pic
    clogo = os.path.join(os.path.dirname(curdir),clogo)
    # opts['clogo'] = clogo
    opts['cname'] = 'MANGO & PEAR ENTERPRISE LTD DEALERS IN FRUITS'
    opts['cinfo'] = '+263111111 / +26311111'
    opts['cloc'] = ''
    # time
    opts['rdate'] = string_to_date(opts['rdate'])
    receipt.print_header(opts)
    receipt.print_items(items)
    receipt.print_message('THANKS FOR YOUR PATRONAGE')
    receipt.print_vat('Amount is VAT INCLUSIVE')
    receipt.print_me('Programmed by : Softwares. : +263111111')
    receipt.esecute()
    receipt.escut()
    receipt.estop()

def string_to_date(string):
    date_time = string.split('T')
    date = tuple([int(x) for x in date_time[0].split('-')])
    time = tuple([int(x) for x in date_time[1].split('.')[0].split(':')])
    string = datetime.datetime(*date,*time).strftime('%a %b %d %I:%M:%S %p %Y')
    return string
