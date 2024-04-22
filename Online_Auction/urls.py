from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from auction.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('user_home',Bidder_Home,name="user_home"),
    path('trainer_home',Auction_User,name="trainer_home"),
    path('login_user',Login_User,name="login_user"),
    path('contact',Contact,name="conRtact"),
    path('about',About,name="about"),
    path('contact',Contact,name="contact"),
    path('edit_profile',Edit_Profile,name="edit_profile"),
    path('edit_profile1',Edit_Profile1,name="edit_profile1"),
    path('logout', Logout, name="logout"),
    path('login_admin',Login_Admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('change_password',Change_Password,name="change_password"),
    path('change_password1',Change_Password1,name="change_password1"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('feedback', Feedback,name="feedback"),
    path('add_product', Add_Product,name="add_product"),
    path('new_product', New_product,name="new_product"),
    path('bidder_user', Bidder_User,name="bidder_user"),
    path('view_popup', view_popup,name="view_popup"),
    path('seller_user', Seller_User,name="seller_user"),
    path('all_product2', All_product2,name="all_product2"),
    path('profile', profile, name='profile'),
    path('result', result, name='result'),
    path('view_auction(<int:pid>)', view_auction, name='view_auction'),
    path('particpated_user(<int:pid>)', Participated_user, name='particpated_user'),
    path('google_pay(<int:pid>)', Google_pay, name='google_pay'),
    path('payment2(<int:pid>)', Credit_Card, name='payment2'),
    path('profile1', Profile1, name='profile1'),
    path('status(<int:pid>)', Change_status, name='status'),
    path('winner(<int:pid>)', Winner,name='winner'),
    path('winner2(<int:pid>)', Winner2,name='winner2'),
    path('winner1(<int:pid>)', Winner1,name='winner1'),
    path('start_auction(<int:pid>)', Start_Auction, name='start_auction'),
    path('view_category', view_category, name='view_category'),
    path('view_feedback', view_feedback, name='view_feedback'),
    path('view_subcategory', view_subcategory, name='view_subcategory'),
    path('view_session_date', view_session_date, name='view_session_date'),
    path('view_session_time', view_session_time, name='view_session_time'),
    path('add_category', Add_Category, name='add_category'),
    path('Member_Credit_Card', Member_Credit_Card, name='Member_Credit_Card'),
    path('Member_Google_pay', Member_Google_pay, name='Member_Google_pay'),
    path('Member_Payment_mode', Member_Payment_mode, name='Member_Payment_mode'),
    path('Payment_mode(<int:pid>)', Payment_mode, name='Payment_mode'),
    path('add_subcategory', Add_SubCategory, name='add_subcategory'),
    path('add_session_date', Add_Session_date, name='add_session_date'),
    path('add_session_time', Add_Session_time, name='add_session_time'),
    path('bidding_status', Bidding_Status, name='bidding_status'),
    path('bidding_status2', Bidding_Status2, name='bidding_status2'),
    path('all_product', All_product, name='all_product'),
    path('edit_category(<int:pid>)', Edit_Category, name='edit_category'),
    path('product_detail(<int:pid>)', product_detail, name='product_detail'),
    path('edit_subcategory(<int:pid>)', Edit_SubCategory, name='edit_subcategory'),
    path('edit_session_date(<int:pid>)', Edit_Session_date, name='edit_session_date'),
    path('edit_session_time(<int:pid>)', Edit_Session_time, name='edit_session_time'),
    path('delete_category(<int:pid>)', delete_category, name='delete_category'),
    path('delete_feedback(<int:pid>)', delete_feedback, name='delete_feedback'),
    path('delete_subcategory(<int:pid>)', delete_subcategory, name='delete_subcategory'),
    path('delete_session_date(<int:pid>)', delete_session_date, name='delete_session_date'),
    path('delete_session_time(<int:pid>)', delete_session_time, name='delete_session_time'),
    path('load-courses/', load_courses, name='ajax_load_courses'),
    path('load-courses1/', load_courses1, name='ajax_load_courses1'),
    path('product_detail2(<int:pid>)', product_detail2, name='product_detail2'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
