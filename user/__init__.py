from flask import Blueprint
user=Blueprint('user',
                   __name__,
                   )
import views
import models