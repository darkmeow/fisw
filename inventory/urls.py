from django.conf.urls import patterns, include, url
from inventory import views
from django.contrib import admin


'''
urlpatterns for inventory app:
        (base_url/*                             ,'inventory.views.FILE.MODULE', options)
'''
urlpatterns = patterns('',
    url(r'^userdata.csv'                        ,'inventory.views.csv.grafico_user'),
    url(r'^testing.csv'                         ,'inventory.views.csv.grafico'),
    url(r'^testing/'                            ,'inventory.views.testing.grafico'),
    url(r'^mailbonito/$'                        ,'inventory.views.mandrill_mail.mailbonito'),
    url(r'^$'                                   ,'inventory.views.user.index'),
    url(r'^wcg_login/$'                         ,'inventory.views.user.wcg_login'),
    url(r'^dashboard'                           ,'inventory.views.user.dashboard'),
    url(r'^register_item/$'                     ,'inventory.views.items.register_item'),
    url(r'^list_items/$'                        ,'inventory.views.items.list_items', name='items_list'),
    url(r'^item/(?P<id_item>[0-9]+)/$'          ,'inventory.views.items.item', name='item_details'),
    url(r'^edit_item/(?P<id_item>[0-9]+)/$'     ,'inventory.views.items.edit_item'),
    url(r'^search_items/$'                        ,'inventory.views.items.search_item'),
    url(r'^search_item_ajax/$'                  ,'inventory.views.items.search_item_ajax'),
    url(r'^list_loans/$'                        ,'inventory.views.loans.list_loans', name='loans_list'),
    url(r'^loan/(?P<id_loan>[0-9]+)/$'          ,'inventory.views.loans.loan', name='loan_details'),
    url(r'^register_loan/$'                     ,'inventory.views.loans.register_loan'),
    url(r'^return_loan/(?P<id_loan>[0-9]+)/$'   ,'inventory.views.loans.return_loan'),
    url(r'^loan_cancel_list/$'                  ,'inventory.views.loans.loan_cancel_list'),
    url(r'^loan_cancel_list_ajax'               ,'inventory.views.loans.loan_cancel_list_ajax'),
    url(r'history_loan/$'                      ,'inventory.views.loans.loan_history'),
)