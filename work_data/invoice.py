

from work_data.printer_test_web import text_print
from work_data.eps_printer_test_web import dummy_print

def print_invoice(items, opts):
    text_print(items, opts)
