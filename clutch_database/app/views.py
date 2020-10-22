from flask import flash, render_template, g
from flask_appbuilder.actions import action
from flask_babel import lazy_gettext as _
from . import appbuilder, db
from .models import Addresses, BenefitPlanUsers, BenefitPlans, Carriers, Locations, InsuranceProviders, Insurances, Prescribers, Prescriptions, PrescriptionStatus, Users
#from .models import Addresses, BenefitPlanUsers, BenefitPlans, Carriers, ChangeAdditionalPharmacyPrcingRecords, ChangeAdditionalSubmittedValuesRecords, ChangeClaimBalancesRecords, ChangeClaimIndicatorRecords, ChangeClaimRecords, ChangeClaimRejectRecords, ChangeDrugClassificationRecords, ChangeDurRecords, ChangeEnhancedPrescriberRecords, ChangeEnhancedSubmittedMemberRecords, ChangeMultiIngredientCompoundRecords, ChangePaperClaimInfoRecords, ChangePatientInfoRecords, ChangePatientPayRecords, ChangePharmacyPricingRecords, ChangePharmacyRecords, ChangePlanCodesUsedRecords, ChangePriorAuthorizationRecords, ChangeSubmittedCobClaimInfoRecords, ChangeSubmittedDurOverrideRecords, Locations, ImaAccumulatorRecords, ImaEligibilityRecords, InsuranceProviders, Insurances, NcpdpTerminologies, PrescriptionsHeader, PrescriptionsDetail, PrescriptionStatus, SurescriptsMessages, SurescriptsOrganizations, SurescriptsProviderLocations, SurescriptsRequests, Users
from flask_appbuilder import MasterDetailView, ModelView, SimpleFormView, MultipleView, BaseView, expose, ModelRestApi, CompactCRUDMixin
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy import create_engine
from wtforms.ext.sqlalchemy.orm import model_form
from sqlalchemy.orm import Query, scoped_session, sessionmaker
from flask_admin.contrib.sqla.filters import BaseSQLAFilter, FilterEqual
from flask import redirect
from flask_appbuilder.api import BaseApi, expose, rison
import uuid
import json
import datetime
from flask_appbuilder.models.filters import BaseFilter
from flask_appbuilder.models.sqla.filters import FilterInFunction, FilterEqualFunction


#def get_user_id():
#    return g.user.id


class AddressesModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Addresses)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]
    edit_columns = ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]
    list_columns = ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]
    
    
class AddressesModelApi(ModelRestApi):
    resource_name = 'addresses_model_api'
    datamodel = SQLAInterface(Addresses)
#    add_columns = ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]
#    edit_columns = ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]
#    list_columns = ["id", "street1", "street2", "state", "city", "zip_code", "latitude", "longitude", "county_fips", "state_fips"]


class BenefitPlanUsersModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(BenefitPlanUsers)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "benefit_plan_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]
    edit_columns = ["id", "benefit_plan_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]
    list_columns = ["id", "benefit_plan_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "benefit_plan_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]
    
    
class BenefitPlanUsersModelApi(ModelRestApi):
    resource_name = 'benefit_plan_users_model_api'
    datamodel = SQLAInterface(BenefitPlanUsers)
#    add_columns = ["id", "benefit_plan_id", "user_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]
#    edit_columns = ["id", "benefit_plan_id", "user_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]
#    list_columns = ["id", "benefit_plan_id", "user_id", "relation", "member_number", "person_code", "out_of_pocket_accumulator", "coverage_level", "accumulator_adjusted_on", "deductible_accumulator"]
    



class BenefitPlansModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(BenefitPlans)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]
    edit_columns = ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]
    list_columns = ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]
 
class BenefitPlansModelApi(ModelRestApi):
    resource_name = 'benefit_plans_model_api'
    datamodel = SQLAInterface(BenefitPlans)
#    add_columns = ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]
#    edit_columns = ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]
#    list_columns = ["id", "carrier_id", "name", "rx_group", "medical_group", "individual_deductible", "individual_max_out_of_pocket", "eligibility_last_processed_at", "eligibility_last_updated_at", "plan_code", "claim_upload_schedule", "accumulator_last_processed_at", "family_deductible", "family_max_out_of_pocket", "deductible_term", "max_out_of_pocket_term"]
 
    

class CarriersModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Carriers)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]
    edit_columns = ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]
    list_columns = ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]

class CarriersModelApi(ModelRestApi):
    resource_name = 'carriers_model_api'
    datamodel = SQLAInterface(Carriers)
#    add_columns = ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]
#    edit_columns = ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]
#    list_columns = ["id", "name", "bin", "pcn", "pricing_network", "category", "customer_care_phone", "pharmacy_help_phone"]

    

class LocationsModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Locations)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]
    edit_columns = ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]
    list_columns = ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]

class LocationsModelApi(ModelRestApi):
    resource_name = 'locations_model_api'
    datamodel = SQLAInterface(Locations)
#    add_columns = ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]
#    edit_columns = ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]
#    list_columns = ["id", "name", "store_number", "phone", "department", "npi", "fax", "address_id"]

   
    

class InsuranceProvidersModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(InsuranceProviders)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "name", "trading_partner_id"]
    edit_columns = ["id", "name", "trading_partner_id"]
    list_columns = ["id", "name", "trading_partner_id"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "name", "trading_partner_id"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]

class InsuranceProvidersModelApi(ModelRestApi):
    resource_name = 'insurance_providers_model_api'
    datamodel = SQLAInterface(InsuranceProviders)
#    add_columns = ["id", "name", "trading_partner_id"]
#    edit_columns = ["id", "name", "trading_partner_id"]
#    list_columns = ["id", "name", "trading_partner_id"]
    


class InsurancesModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Insurances)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]
    edit_columns = ["id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]
    list_columns = ["id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]

class InsurancesModelApi(ModelRestApi):
    resource_name = 'insurance_model_api'
    datamodel = SQLAInterface(Insurances)
#    add_columns = ["id", "user_id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]
#    edit_columns = ["id", "user_id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]
#    list_columns = ["id", "user_id", "insurance_provider_id", "rx_bin", "rx_pcn", "rx_group", "member_id", "eligibility_response"]
    



class Prescriptions(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(PrescriptionsHeader)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id", "prescriber_id", "drug", "drug_name", "dose_form", "dose_strength", "dosage_frequency", "dosage_frequency_text", "dosage_frequency_uom", "dosage_method", "dosage_quantity", "dosage_quantity_uom", "dosage_route_of_administration", "quantity", "quantity_uom", "quantity_uom_code", "strength", "strength_uom", "strength_uom_code", "substitutions", "name", "description", "ndc", "sig", "awp", "generic_ndc", "generic_drug_name", "generic_awp", "transfer_price", "controlled_substance_class", "daw_code", "test", "notes", "days_supply"]
    edit_columns = ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id", "prescriber_id", "drug", "drug_name", "dose_form", "dose_strength", "dosage_frequency", "dosage_frequency_text", "dosage_frequency_uom", "dosage_method", "dosage_quantity", "dosage_quantity_uom", "dosage_route_of_administration", "quantity", "quantity_uom", "quantity_uom_code", "strength", "strength_uom", "strength_uom_code", "substitutions", "name", "description", "ndc", "sig", "awp", "generic_ndc", "generic_drug_name", "generic_awp", "transfer_price", "controlled_substance_class", "daw_code", "test", "notes", "days_supply"]
    list_columns = ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id", "prescriber_id", "drug", "drug_name", "dose_form", "dose_strength", "dosage_frequency", "dosage_frequency_text", "dosage_frequency_uom", "dosage_method", "dosage_quantity", "dosage_quantity_uom", "dosage_route_of_administration", "quantity", "quantity_uom", "quantity_uom_code", "strength", "strength_uom", "strength_uom_code", "substitutions", "name", "description", "ndc", "sig", "awp", "generic_ndc", "generic_drug_name", "generic_awp", "transfer_price", "controlled_substance_class", "daw_code", "test", "notes", "days_supply"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id", "prescriber_id", "drug", "drug_name", "dose_form", "dose_strength", "dosage_frequency", "dosage_frequency_text", "dosage_frequency_uom", "dosage_method", "dosage_quantity", "dosage_quantity_uom", "dosage_route_of_administration", "quantity", "quantity_uom", "quantity_uom_code", "strength", "strength_uom", "strength_uom_code", "substitutions", "name", "description", "ndc", "sig", "awp", "generic_ndc", "generic_drug_name", "generic_awp", "transfer_price", "controlled_substance_class", "daw_code", "test", "notes", "days_supply"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]

class PrescriptionsModelApi(ModelRestApi):
    resource_name = 'prescriptions_model_api'
    datamodel = SQLAInterface(Prescriptions)
#    add_columns = ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id"]
#    edit_columns = ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id"]
#    list_columns = ["id", "patient_name", "patient_first_name", "patient_middle_name", "patient_last_name", "patient_suffix", "patient_date_of_birth", "patient_sex", "patient_address_street1", "patient_address_city", "patient_address_state", "patient_address_zip_code", "patient_email", "patient_phone", "patient_cell_phone", "primary_payer_person_code", "refills_authorized", "refills_remaining", "rx_number", "new", "transferred_at", "filled_at", "dispensed_at", "canceled_at", "claim_number", "reversal_number", "reversed_at", "written_on", "prior_authorization", "prior_authorization_status_code", "user_id", "location_id", "prescription_status_id"]
    

class Prescribers(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Prescribers)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "category", "npi", "dea_number", "state_license_number", "first_name", "middle_name", "last_name", "suffix", "address_id", "phone", "phone_extension", "fax", "fax_extension", "specialty_code", "specialty"]
    edit_columns = ["id", "category", "npi", "dea_number", "state_license_number", "first_name", "middle_name", "last_name", "suffix", "address_id", "phone", "phone_extension", "fax", "fax_extension", "specialty_code", "specialty"]
    list_columns = ["id", "category", "npi", "dea_number", "state_license_number", "first_name", "middle_name", "last_name", "suffix", "address_id", "phone", "phone_extension", "fax", "fax_extension", "specialty_code", "specialty"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "category", "npi", "dea_number", "state_license_number", "first_name", "middle_name", "last_name", "suffix", "address_id", "phone", "phone_extension", "fax", "fax_extension", "specialty_code", "specialty"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]
    
    
    
class PrescribersModelApi(ModelRestApi):
    resource_name = 'prescribers_model_api'
    datamodel = SQLAInterface(Prescribers)



class PrescriptionStatusModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(PrescriptionStatus)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["id", "prescription_status"]
    edit_columns = ["id", "prescription_status"]
    list_columns = ["id", "prescription_status"]
    
    show_fieldsets = [
        ("Info", {"fields": ["id", "prescription_status"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]
    
class PrescriptionStatusModelApi(ModelRestApi):
    resource_name = 'prescription_status_model_api'
    datamodel = SQLAInterface(PrescriptionStatus)
#    add_columns = ["id", "prescription_status"]
#    edit_columns = ["id", "prescription_status"]
#    list_columns = ["id", "prescription_status"]
    



class UsersModelView(CompactCRUDMixin, ModelView):
    datamodel = SQLAInterface(Users)
    
    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"
    
    add_columns = ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]
    edit_columns = ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]
    list_columns = ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]
    
    show_fieldsets = [
        ("Info", {"fields": ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]}),
        (
            "Audit",
            {
                "fields": ["created_by", "created_on", "changed_by", "changed_on"],
            },
        ),
    ]

class UsersModelApi(ModelRestApi):
    resource_name = 'users_model_api'
    datamodel = SQLAInterface(Users)
#    add_columns = ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]
#    edit_columns = ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]
#    list_columns = ["sex", "date_of_birth", "phone", "phone_extension", "password_digest", "must_update_password", "phone_verification_code", "phone_verified_code", "phone_verified_at", "middle_initial", "suffix", "registration_code", "height", "weight", "race_code", "ethnicity_code", "physician_specialty", "physician_specialty_code", "physician_fax", "physician_fax_extension", "physician_npi", "physician_dea", "physician_state_license", "physician_supervisor", "user_address_id", "location_id"]
    




db.create_all()




appbuilder.add_view(
    AddressesModelView,
    "Addresses",
    icon="fa-table"
)

appbuilder.add_api(AddressesModelApi)


appbuilder.add_view(
    BenefitPlanUsersModelView,
    "Benefit Plan Users",
    icon="fa-table"
)

appbuilder.add_api(BenefitPlanUsersModelApi)

appbuilder.add_view(
    BenefitPlansModelView,
    "Benefit Plans",
    icon="fa-table"
)

appbuilder.add_api(BenefitPlansModelApi)

appbuilder.add_view(
    CarriersModelView,
    "Carriers",
    icon="fa-table"
)

appbuilder.add_api(CarriersModelApi)

appbuilder.add_view(
    LocationsModelView,
    "Locations",
    icon="fa-table"
)

appbuilder.add_api(LocationsModelApi)

appbuilder.add_view(
    InsuranceProvidersModelView,
    "Insurance Providers",
    icon="fa-table"
)

appbuilder.add_api(InsuranceProvidersModelApi)


appbuilder.add_view(
    InsurancesModelView,
    "Insurances",
    icon="fa-table"
)

appbuilder.add_api(InsurancesModelApi)

appbuilder.add_view(
    PrescribersModelView,
    "Prescribers",
    icon="fa-table"
)

appbuilder.add_api(PrescribersModelApi)

appbuilder.add_view(
    PrescriptionsModelView,
    "Prescriptions ",
    icon="fa-table"
)

appbuilder.add_api(PrescriptionsModelApi)

appbuilder.add_view(
    PrescriptionStatusModelView,
    "Prescription Status",
    icon="fa-table"
)

appbuilder.add_api(PrescriptionsDetailModelApi)

appbuilder.add_view(
    UsersModelView,
    "Users",
    icon="fa-table"
)

appbuilder.add_api(UsersModelApi)






