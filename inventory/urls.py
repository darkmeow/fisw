from django.conf.urls import patterns, include, url
from inventory import views

'''
urlpatterns for inventory app:
        (base_url/*                             ,'inventory.views.FILE.MODULE', options)
'''
urlpatterns = patterns('',
    url(r'^$'                                   ,'inventory.views.user.index'),
    url(r'^wcg_login/$'                         ,'inventory.views.user.wcg_login'),
    url(r'^dashboard'                           ,'inventory.views.user.dashboard'),
    url(r'^register_item/$'                     ,'inventory.views.items.register_item'),
    url(r'^list_items/$'                        ,'inventory.views.items.list_items', name='items_list'),
    url(r'^item/(?P<id_item>[0-9]+)/$'          ,'inventory.views.items.item', name='item_details'),
    url(r'^list_loans/$'                        ,'inventory.views.loans.list_loans', name='loans_list'),
    url(r'^loan/(?P<id_loan>[0-9]+)/$'          ,'inventory.views.loans.loan', name='loan_details'),
    url(r'^register_loan/$'                     ,'inventory.views.loans.register_loan'),
    url(r'^return_loan/(?P<id_loan>[0-9]+)/$'   ,'inventory.views.loans.return_loan'),
    url(r'^loan_cancel_list/$'                  ,'inventory.views.loans.loan_cancel_list'),
    url(r'^loan_cancel_list_ajax'               ,'inventory.views.loans.loan_cancel_list_ajax'),
)