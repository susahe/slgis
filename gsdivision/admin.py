from django.contrib import admin
from django import forms
# Register your models here.
from .models import *
class DistrctModelForm(forms.ModelForm):
	class Meta:
		model = District
		fields ='__all__'
	def __init__ (self, *args, **kwargs):
		super(DistrictModelForm,self).__init__(*args, **kwargs)

class GramaSevaDivisionAdmin(admin.ModelAdmin):
        ordering = ['gs_name']
        search_fields = ['gs_name','gs_division']
        date_hierarchy = 'gs_start_date'
        list_filter = ['gs_name','gs_division','gs_start_date','gs_end_date']



class VillageAdmin(admin.ModelAdmin):
        #ordering = ['v_name']
        search_fields = ['v_name','v_road']
        list_display = ['v_name', 'v_road']
        list_filter = ['v_name','v_road']



class VillagerAdmin(admin.ModelAdmin):
        #ordering = ['p_type', 'Person.fname']
        search_fields = ['p_type','p_donation']
        list_filter = ['p_donation']

class HouseAdmin(admin.ModelAdmin):
        ordering = ['h_shade']
        search_fields = ['h_shade','h_floor','h_wall','h_water','h_elec','h_toilet','h_lantel']

class LandAdmin(admin.ModelAdmin):
        ordering = ['l_period']
        search_fields = ['l_period','l_type','l_lno','l_kno','l_size']

class OrganizationsAdmin(admin.ModelAdmin):
        ordering = ['o_name']
        search_fields = ['o_name','o_purpose','o_address1','o_address2','o_address3','o_rnumber','o_sdate','o_nmembers','o_sstaff','o_pstaff','o_apstaff','o_tstaff']

class BuisnessAdmin(admin.ModelAdmin):
        ordering = ['b_name']
        search_fields = ['b_name','b_oname','b_paddress1','b_paddress2','b_paddress3','b_type','b_sdate','b_rnumber','b_tnumber']

admin.site.register(GramasevaDivision,GramaSevaDivisionAdmin)
admin.site.register(Village,VillageAdmin)
admin.site.register(Buisness,BuisnessAdmin)
admin.site.register(Organizations,OrganizationsAdmin)
admin.site.register(House,HouseAdmin)
admin.site.register(Land,LandAdmin)
admin.site.register(Villager,VillagerAdmin)
admin.site.register(District)
admin.site.register(DivisionSectOffice)
