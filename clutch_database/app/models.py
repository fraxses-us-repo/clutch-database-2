from flask_appbuilder.security.sqla.models import User
from flask import Markup, url_for
from sqlalchemy.dialects.postgresql import UUID
from flask_appbuilder.filemanager import get_file_original_name
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from flask_appbuilder.models.mixins import AuditMixin, FileColumn
from flask_appbuilder import Model
from datetime import datetime
import uuid
from markupsafe import Markup
from flask_appbuilder.models.decorators import renders
from sqlalchemy import PrimaryKeyConstraint, Column, Integer, String, ForeignKey, Date, Boolean, DateTime, Float, Text, Table, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from flask_appbuilder.models.decorators import renders
from sqlalchemy.orm import scoped_session, sessionmaker, Query
from flask_appbuilder.filemanager import get_file_original_name
from . import appbuilder, db


#class ActiveAdminComments(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'active_admin_comments'
#
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#	namespace = Column('namespace', String(140))
#	body = Column('body', String(140))
#    resource_type = Column('resource_type', String(140))
#    resource_id = Column('resource_id', Integer)
#    author_type = Column('author_type', String(140))
#    author_id = Column('author_id', Integer)
#	
#    def __repr__(self):
#        return self.active_admin_comments

class UserType(AuditMixin, Model):
    __bind_key__ = 'app'
    __tablename__ = 'user_type'
    
    user_type_id = Column('user_type_id', Integer, primary_key=True, autoincrement=True)
    user_type_name = Column('user_type_name', String(140))
    
    def __repr__(self):
        return self.user_type_name
        
class EthnicityCode(Model):
    ethnicity_code_id = Column(Integer, primary_key=True)
    ethnicity_code = Column(String(5), unique=True)
    ethnicity_description = Column(String(20), unique=True)
    def __repr__(self):
        return self.ethnicity_description


class RaceCode(Model):
    race_code_id = Column(Integer, primary_key=True)
    race_code = Column(String(5), unique=True)
    race_description = Column(String(20), unique=True)
    def __repr__(self):
        return self.race_description

class Sex(Model):
    sex_id = Column(Integer, primary_key=True)
    sex_code = Column(String(5), unique=True)
    sex_description = Column(String(20), unique=True)
    def __repr__(self):
        return self.sex_description
        

class Users(User, Model):
    __bind_key__ = 'app'
    __tablename__ = 'ab_user'
    
    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True) 
    #sex = Column('sex', String(140))
    date_of_birth = Column('date_of_birth', Date)
    phone = Column('phone', String(140))
    phone_extension = Column('phone_extension', String(140))
    middle_initial = Column('middle_initial', String(140))
    suffix = Column('suffix', String(140))
    registration_code = Column('registration_code', String(140))
    height = Column('height', Integer)
    weight = Column('weight', Float)
    #race_code = Column('race_code', String(140))
    #ethnicity_code = Column('ethnicity_code', String(140))
    physician_specialty = Column('physician_specialty', String(140))
    physician_specialty_code = Column('physician_specialty_code', String(140))
    physician_fax = Column('physician_fax', String(140))
    physician_fax_extension = Column('physician_fax_extension', String(140))
    physician_npi = Column('physician_npi', String(140))
    physician_dea = Column('physician_dea', String(140))
    physician_state_license = Column('physician_state_license', String(140))
    physician_supervisor = Column('physician_supervisor', String(140))
    
#    insurance_id = Column('insurance_id', Integer, ForeignKey("insurances.insurance_id"), nullable=False)
#    insurances = relationship("Insurances")
#    
#    benefit_plan_user_id = Column('benefit_plan_user_id', Integer, ForeignKey("benefit_plan_users.benefit_plan_user_id"), nullable=False)
#    benefit_plan_users = relationship("BenefitPlanUsers")
    
#    address_id = Column('address_id', Integer, ForeignKey("addresses.id"), nullable=False)
#    addresses = relationship("Addresses")
    
#    entity_id = Column('entity_id', Integer, ForeignKey("entities.entity_id"), nullable=False)
#    entities = relationship("Entities")
    
    user_type_id = Column('user_type_id', Integer, ForeignKey("user_type.user_type_id"), nullable=False)
    user_type = relationship("UserType")
    
    sex_id = Column('sex_id', Integer, ForeignKey("sex.sex_id"), nullable=False)
    sex = relationship("Sex")
    
    race_code_id = Column('race_code_id', Integer, ForeignKey("race_code.race_code_id"), nullable=False)
    race_code = relationship("RaceCode")
    
    ethnicity_code_id = Column('ethnicity_code_id', Integer, ForeignKey("ethnicity_code.ethnicity_code_id"), nullable=False)
    ethnicity_code = relationship("EthnicityCode")
    
    def __repr__(self):
        return str(self.user_id)


#class Addresses(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'addresses'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    street1 = Column('street1', String(140))
#    street2 = Column('street2', String(140))
#    state = Column('state', String(140))
#    city = Column('city', String(140))
#    zip_code = Column('zip_code', String(140))
#    latitude = Column('latitude', Float(precision=None, asdecimal=False, decimal_return_scale=None))
#    longitude = Column('longitude', Float(precision=None, asdecimal=False, decimal_return_scale=None))
#    county_fips = Column('county_fips', String(140))
#    state_fips = Column('state_fips', String(140))
#    
##    address_type_id = Column('address_type_id', Integer, ForeignKey("address_type.address_type_id"), nullable=False)
##    address_type = relationship("AddressType")
#    
#    #user_address_relationship = relationship('Users', foreign_keys='Users.user_address_id')
#    
#    def __repr__(self):
#        return str(self.addresses_id)
#    
#class AddressType(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'address_type'
#    
#    address_type_id = Column('address_type_id', Integer, primary_key=True, autoincrement=True)
#    address_type = Column('address_type', String(140))
    
#    def __repr__(self):
#        return str(self.address_type)
        
#class AdminUsers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'admin_users'
#
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    email = Column('email', String(140))
#    encrypted_password = Column('encrypted_password', String(140))
#    reset_password_token = Column('reset_password_token', String(140))
#    reset_password_sent_at = Column('reset_password_sent_at', DateTime)
#    remember_created_at = Column('remember_created_at', DateTime)
#    sign_in_count = Column('sign_in_count', Integer)
#    current_sign_in_at = Column('current_sign_in_at', DateTime)
#    last_sign_in_at = Column('last_sign_in_at', DateTime)
#    current_sign_in_ip = Column('current_sign_in_ip', String(140))
#    last_sign_in_ip = Column('last_sign_in_ip', String(140))
#    failed_attempts = Column('failed_attempts', Integer)
#    unlock_token = Column('unlock_token', String(140))
#    locked_at = Column('locked_at', DateTime)
#    role = Column('role', String(140))
#
#    def __repr__(self):
#        return self.admin_users
#        
#class ArInternalMetadata(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'ar_internal_metadata'
#        
#    key = Column('key', String(140), primary_key=True)
#    value = Column('value', String(140))
#    
#    def __repr__(self):
#        return self.ar_internal_metadata
#        
#class BenefitPlanUsers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'benefit_plan_users'
#    
#    benefit_plan_users_id = Column('benefit_plan_users_id', Integer, primary_key=True, autoincrement=True)
#    #benefit_plan_id = Column('benefit_plan_id', Integer)
#    #user_id = Column('user_id', Integer)
#    relation = Column('relation', String(140))
#    member_number = Column('member_number', String(140))
#    person_code = Column('person_code', Integer)
#    out_of_pocket_accumulator = Column('out_of_pocket_accumulator', Float)
#    coverage_level = Column('coverage_level', String(140))
#    accumulator_adjusted_on = Column('accumulator_adjusted_on', DateTime)
#    deductible_accumulator = Column('deductible_accumulator', Float)
#       
#    benefit_plan_id = Column('benefit_plan_id', Integer, ForeignKey("benefit_plans.benefit_plan_id"), nullable=False)
#    benefit_plans = relationship("BenefitPlans")
#    
#    def __repr__(self):
#        return str(self.benefit_plan_users)
#        
#class BenefitPlans(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'benefit_plans'
#    
#    benefit_plan_id = Column('benefit_plan_id', Integer, primary_key=True, autoincrement=True)
#    #carrier_id = Column('carrier_id', Integer)
#    name = Column('name', String(140))
#    rx_group = Column('rx_group', String(140))
#    medical_group = Column('medical_group', String(140))
#    individual_deductible = Column('individual_deductible', Float)
#    individual_max_out_of_pocket = Column('individual_max_out_of_pocket', Float)
#    eligibility_last_processed_at = Column('eligibility_last_processed_at', DateTime)
#    eligibility_last_updated_at = Column('eligibility_last_updated_at', DateTime)
#    plan_code = Column('plan_code', String(140))
#    claim_upload_schedule = Column('claim_upload_schedule', String(140))
#    accumulator_last_processed_at = Column('accumulator_last_processed_at', DateTime)
#    family_deductible = Column('family_deductible', Float)
#    family_max_out_of_pocket = Column('family_max_out_of_pocket', Float)
#    deductible_term = Column('deductible_term', String(140))
#    max_out_of_pocket_term = Column('max_out_of_pocket_term', String(140))
#    
#    carrier_id = Column('carrier_id', Integer, ForeignKey("carriers.carrier_id"), nullable=False)
#    carriers = relationship("Carriers")
#    
#    def __repr__(self):
#        return self.benefit_plans
#        
#class BlacklistedTokens(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'blacklisted_tokens'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    token = Column('token', String(140))
#    
#    def __repr__(self):
#        return self.token
#    
#class Carriers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'carriers'
#
#    carrier_id = Column('id', Integer, primary_key=True, autoincrement=True)
#    name = Column('name', String(140))
#    bin = Column('bin', String(140))
#    pcn = Column('pcn', String(140))
#    pricing_network = Column('pricing_network', String(140))
#    category = Column('category', String(140))
#    customer_care_phone = Column('customer_care_phone', String(140))
#    pharmacy_help_phone = Column('pharmacy_help_phone', String(140))
#    
#    def __repr__(self):
#        str(return self.carriers)
#		
#class ChangeAdditionalPharmacyPricingRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_additional_pharmacy_pricing_records'
#	
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    submitted_u_and_c = Column('submitted_u_and_c', Float)
#    submitted_ingredient_cost = Column('submitted_ingredient_cost', Float)
#    submitted_dispensing_fee = Column('submitted_dispensing_fee', Float)
#    submitted_sales_tax = Column('submitted_sales_tax', Float)
#    submitted_gross_amount = Column('submitted_gross_amount', Float)
#    submitted_copay_amount = Column('submitted_copay_amount', Float)
#    reserved = Column('reserved', String(140))
#	
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#    
#    def __repr__(self):
#        return self.change_additional_pharmacy_pricing_records
#		
#class ChangeAdditionalSubmittedValuesRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_additional_submitted_values_records'
#	
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    submitted_ndc_number = Column('submitted_ndc_number', String(140))
#    submitted_cardholder_id = Column('submitted_cardholder_id', String(140))
#    prescription_origin_code = Column('prescription_origin_code', Integer)
#    primary_other_payer_id_qualifier = Column('primary_other_payer_id_qualifier', Integer)
#    primary_other_payer_id = Column('primary_other_payer_id', Integer)
#    submitted_ncpdp_version = Column('submitted_ncpdp_version', String(140))
#    submitted_group_number = Column('submitted_group_number', String(140))
#    submitted_bin = Column('submitted_bin', String(140))
#    submitted_transaction_type = Column('submitted_transaction_type', String(140))
#    software_vendor_id = Column('software_vendor_id', String(140))
#    reserved = Column('reserved', String(140))
#   
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    def __repr__(self):
#        return self.change_additional_submitted_values_records
#		
#class ChangeClaimBalancesRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_claim_balances_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    individual_deductible_amount = Column('individual_deductible_amount', Float)
#    individual_member_amount = Column('individual_member_amount', Float)
#    individual_sponsor_amount = Column('individual_sponsor_amount', Float)
#    individual_starting_deductible_accumulation = Column('individual_starting_deductible_accumulation', Float)
#    individual_ending_deductible_accumulation = Column('individual_ending_deductible_accumulation', Float)
#    individual_remaining_deductible_amount = Column('individual_remaining_deductible_amount', Float)
#    individual_starting_member_accumulation = Column('individual_starting_member_accumulation', Float)
#    individual_ending_member_accumulation  = Column('individual_ending_member_accumulation', Float)
#    individual_starting_sponsor_accumulation = Column('individual_starting_sponsor_accumulation',  Float)
#    individual_ending_sponsor_accumulation = Column('individual_ending_sponsor_accumulation', Float)
#    individual_starting_tier_level = Column('individual_starting_tier_level', Integer)
#    individual_ending_tier_level = Column('individual_ending_tier_level', Integer)
#    family_deductible_amount = Column('family_deductible_amount', Float)
#    family_member_amount = Column('family_member_amount', Float)
#    family_sponsor_amount = Column('family_sponsor_amount', Float)
#    family_starting_deductible_accumulation = Column('family_starting_deductible_accumulation', Float)
#    family_ending_deductible_accumulation = Column('family_ending_deductible_accumulation', Float)
#    family_remaining_deductible_amount = Column('family_remaining_deductible_amount', Float)
#    family_starting_member_accumulation = Column('family_starting_member_accumulation', Float)
#    family_ending_member_accumulation  = Column('family_ending_member_accumulation', Float)
#    family_starting_sponsor_accumulation = Column('family_starting_sponsor_accumulation',  Float)
#    family_ending_sponsor_accumulation = Column('family_ending_sponsor_accumulation', Float)
#    family_starting_tier_level = Column('family_starting_tier_level', Integer)
#    family_ending_tier_level = Column('family_ending_tier_level', Integer)
#    card_value = Column('card_value', Float)
#    rebate_adjustment = Column('rebate_adjustment', Float)
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_claim_balances_records
#
#class ChangeClaimIndicatorRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_claim_indicator_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    paper_claim_flag = Column('paper_claim_flag', Integer)
#    direct_reimbursement_flag = Column('direct_reimbursement_flag', Integer)
#    test_claim_flag = Column('test_claim_flag', Integer)
#    batch_processed_flag = Column('batch_processed_flag', Integer)
#    other_processed_flag = Column('other_processed_flag', Integer)
#    formulary_drug_flag = Column('formulary_drug_flag', Integer)
#    network_pharmacy_flag = Column('network_pharmacy_flag', Integer)
#    network_physician_flag = Column('network_physician_flag', Integer)
#    shoebox_claim_flag = Column('shoebox_claim_flag', Integer)
#    product_quantity_claim_flag = Column('product_quantity_claim_flag', Integer)
#    starter_dose_flag = Column('starter_dose_flag', Integer)
#    prior_auth_flag = Column('prior_auth_flag', Integer)
#    dur_flag = Column('dur_flag', Integer)
#    dur_override_flag = Column('dur_override_flag', Integer)
#    ig_copay_flag = Column('ig_copay_flag', Integer)
#    multi_ingredient_compound_flag = Column('multi_ingredient_compound_flag', Integer)
#    partial_file_dispensing_status = Column('partial_file_dispensing_status', Integer)
#    medicaid_flag = Column('medicaid_flag', Integer)
#    force_u_and_c_flag = Column('force_u_and_c_flag', Integer)
#    ndc_remapped = Column('ndc_remapped', Integer)
#    force_0_pharmacy_due = Column('force_0_pharmacy_due', Integer)
#    additional_lower_of_state_rate_used = Column('additional_lower_of_state_rate_used', Integer)
#    pos_medicaid_flag = Column('pos_medicaid_flag', Integer)
#    alternate_processing_bypass = Column('alternate_processing_bypass', Integer)
#    tax_exempt_indicator = Column('tax_exempt_indicator', Integer)
#    alternate_drug_record = Column('alternate_drug_record', Integer)
#    claim_rounding_used = Column('claim_rounding_used', Integer)
#    medical_claim_indicator = Column('medical_claim_indicator', Integer)
#    compensable_claim_indicator = Column('compensable_claim_indicator', Integer)
#    data_fee_transaction = Column('data_fee_transaction', Integer)
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_claim_indicator_records
#        
#class ChangeClaimRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_claim_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    plan = Column('plan', String(140))
#    claim_authorization_number = Column('claim_authorization_number', String(140))
#    original_claim_authorization_number = Column('original_claim_authorization_number', String(140))
#    reversal_claim_authorization_number = Column('reversal_claim_authorization_number', String(140))
#    date_processed = Column('date_processed', Date)
#    time_processed = Column('time_processed', Date)
#    rejection_flag = Column('rejection_flag', Integer)
#    duplicate_flag = Column('duplicate_flag', Integer)
#    reversal_flag = Column('reversal_flag', Integer)
#    pharmacy_ncpdp_id = Column('pharmacy_ncpdp_id', String(140))
#    pharmacy_name = Column('pharmacy_name', String(140))
#    pharmacy_chain_number = Column('pharmacy_chain_number', String(140))
#    pharmacy_chain_name = Column('pharmacy_chain_name', String(140))
#    pharmacy_type = Column('pharmacy_type', String(140))
#    carrier_code = Column('carrier_code', String(140))
#    submitted_carrier_code = Column('submitted_carrier_code', String(140))
#    tpa_broker_code = Column('tpa_broker_code', String(140))
#    tpa_broker_name = Column('tpa_broker_name', String(140))
#    sponsor_code = Column('sponsor_code', String(140))
#    sponsor_name = Column('sponsor_name', String(140))
#    group_number = Column('group_number', String(140))
#    group_name = Column('group_name', String(140))
#    cardholder_id_number = Column('cardholder_id_number', String(140))
#    patient_person_code = Column('patient_person_code', Integer)
#    patient_last_name = Column('patient_last_name', String(140))
#    patient_first_name = Column('patient_first_name', String(140))
#    prescriber_id = Column('prescriber_id', String(140))
#    prescriber_name = Column('prescriber_name', String(140))
#    date_filled = Column('date_filled', Date)
#    date_written = Column('date_written', Date)
#    rx_number = Column('rx_number', String(140))
#    fill_number = Column('fill_number', Integer)
#    refills_authorized = Column('refills_authorized', Integer)
#    drug_ndc = Column('drug_ndc', String(140))
#    drug_name = Column('drug_name', String(140))
#    drug_strength_description = Column('drug_strength_description', String(140))
#    drug_dose_from_description = Column('drug_dose_from_description', String(140))
#    submitted_compound_code = Column('submitted_compound_code', Integer)
#    submitted_route_of_admin = Column('submitted_route_of_admin', String(140))
#    drug_processed_sig_code = Column('drug_processed_sig_code', String(140))
#    drug_mony_code = Column('drug_mony_code', String(140))
#    quantity_dispensed = Column('quantity_dispensed', Integer)
#    days_supply = Column('days_supply', Integer)
#    daw_code = Column('daw_code', String(140))
#    plan_ingredient_cost = Column('plan_ingredient_cost', Float)
#    plan_dispensing_fee = Column('plan_dispensing_fee', Float)
#    plan_sales_tax = Column('plan_sales_tax', Float)
#    incentive_fee = Column('incentive_fee', Float)
#    processor_fee = Column('processor_fee', Float)
#    plan_gross_amount = Column('plan_gross_amount', Float)
#    other_payer_amount = Column('other_payer_amount', Float)
#    total_patient_pay_amount = Column('total_patient_pay_amount', Float)
#    plan_pharmacy_pay_amount = Column('plan_pharmacy_pay_amount', Float)
#    plan_basis_of_cost = Column('plan_basis_of_cost', String(140))
#    plan_basis_of_reimbursement = Column('plan_basis_of_reimbursement', String(140))
#    calculated_awp = Column('calculated_awp', Float)
#    submission_clarification_code = Column('submission_clarification_code', Integer)
#    other_coverage_code = Column('other_coverage_code', Integer)
#    medicaid_code = Column('medicaid_code', String(140))
#    medicaid_name = Column('medicaid_name', String(140))
#    coupon_number = Column('coupon_number', String(140))
#    pharmacy_npi = Column('pharmacy_npi', String(140))
#    pharmacy_id_qualifier_submitted = Column('pharmacy_id_qualifier_submitted', String(140))
#    calculated_fed_mac = Column('calculated_fed_mac', Float)
#    calculated_awp_source = Column('calculated_awp_source', Integer)
#    calculated_wac = Column('calculated_wac', Float)
#    coupon_actual_use_number = Column('coupon_actual_use_number', Integer)
#    processed_single_source_generic_indicator = Column('processed_single_source_generic_indicator', String(140))
#    manufacturer_name = Column('manufacturer_name', String(140))
#    adjudicated_unit_price = Column('adjudicated_unit_price', Float)
#    pre_copay_rounding_amount = Column('pre_copay_rounding_amount', Float)
#    number_of_coupon_uses = Column('number_of_coupon_uses', Integer)
#    combined_coupon_uses = Column('combined_coupon_uses', Integer)
#    reject_reprocess_original_authorization_number = Column('reject_reprocess_original_authorization_number', String(140))
#    reserved = Column('reserved', String(140))
#    transaction_message = Column('transaction_message', String(140))
#    submitted_at = Column('submitted_at', DateTime)
#    processed_at = Column('processed_at', DateTime)
#    
#    def __repr__(self):
#        return self.change_claim_records
#        
#class ChangeClaimRejectRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_claim_reject_records'
#    
#    id = Column('change_claim_record_id', Integer, primary_key=True, autoincrement=True)
#    reject_code_1 = Column('reject_code_1', String(140))
#    reject_code_2 = Column('reject_code_2', String(140))
#    reject_code_3 = Column('reject_code_3', String(140))
#    reject_code_4 = Column('reject_code_4', String(140))
#    reject_code_5 = Column('reject_code_5', String(140))
#    ecc_reject_code_1 = Column('ecc_reject_code_1', String(140))
#    ecc_reject_code_2 = Column('ecc_reject_code_2', String(140))
#    ecc_reject_code_3 = Column('ecc_reject_code_3', String(140))
#    ecc_reject_code_4 = Column('ecc_reject_code_4', String(140))
#    ecc_reject_code_5 = Column('ecc_reject_code_5', String(140))
#
#    def __repr__(self):
#        return self.change_claim_reject_records
#        
#class ChangeDrugClassificationRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_drug_classification_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    category_code = Column('category_code', String(140))
#    class_code = Column('class_code', String(140))
#    gc1_code = Column('gc1_code', String(140))
#    gc2_code = Column('gc2_code', String(140))
#    gc3_code = Column('gc3_code', String(140))
#    gc4_code = Column('gc4_code', String(140))
#    specific_therapeutic_class = Column('specific_therapeutic_class', String(140))
#    gcn_code = Column('gcn_code', Integer)
#    gcn_sequence_number = Column('gcn_sequence_number', Integer)
#    standard_terapeutic_class = Column('standard_terapeutic_class', Integer)
#    generic_therapeutic_class = Column('generic_therapeutic_class', Integer)
#    ahfs_therapeutic_class = Column('ahfs_therapeutic_class', Integer)
#    orange_book_code = Column('orange_book_code', String(140))
#    route_of_administration_code = Column('route_of_administration_code', String(140))
#    drug_form_code = Column('drug_form_code', Integer)
#    dea_code = Column('dea_code', Integer)
#    maintenance_drug_indicator = Column('maintenance_drug_indicator', Integer)
#    unit_of_use_indicator = Column('unit_of_use_indicator', Integer)
#    repackage_indicator = Column('repackage_indicator', Integer)
#    unit_dose_indicator = Column('unit_dose_indicator', Integer)
#    desi_drug_indicator = Column('desi_drug_indicator', Integer)
#    drug_obsolete_date = Column('drug_obsolete_date', Date)
#    medispan_gpi = Column('medispan_gpi', String(140))
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#    
#    def __repr__(self):
#        return self.change_drug_classification_records
#    
#class ChangeDurRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_dur_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    dur_1_conflict_code = Column('dur_1_conflict_code', String(140))
#    dur_1_severity_index = Column('dur_1_severity_index', String(140))
#    dur_1_hit_disposition = Column('dur_1_hit_disposition', String(140))
#    dur_1_conflict_authorization_number = Column('dur_1_conflict_authorization_number', String(140))
#    dur_2_conflict_code = Column('dur_2_conflict_code', String(140))
#    dur_2_severity_index = Column('dur_2_severity_index', String(140))
#    dur_2_hit_disposition = Column('dur_2_hit_disposition', String(140))
#    dur_2_conflict_authorization_number = Column('dur_2_conflict_authorization_number', String(140))
#    dur_3_conflict_code = Column('dur_3_conflict_code', String(140))
#    dur_3_severity_index = Column('dur_3_severity_index', String(140))
#    dur_3_hit_disposition = Column('dur_3_hit_disposition', String(140))
#    dur_3_conflict_authorization_number = Column('dur_3_conflict_authorization_number', String(140))
#    dur_4_conflict_code = Column('dur_4_conflict_code', String(140))
#    dur_4_severity_index = Column('dur_4_severity_index', String(140))
#    dur_4_hit_disposition = Column('dur_4_hit_disposition', String(140))
#    dur_4_conflict_authorization_number = Column('dur_4_conflict_authorization_number', String(140))
#    dur_5_conflict_code = Column('dur_5_conflict_code', String(140))
#    dur_5_severity_index = Column('dur_5_severity_index', String(140))
#    dur_5_hit_disposition = Column('dur_5_hit_disposition', String(140))
#    dur_5_conflict_authorization_number = Column('dur_5_conflict_authorization_number', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_dur_records
#        
#class ChangeEnhancedPrescriberRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_enhanced_prescriber_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    prescriber_name = Column('prescriber_name', String(140))
#    dea = Column('dea', String(140))
#    npi = Column('npi', String(140))
#    business_activity_code = Column('business_activity_code', String(140))
#    business_activity_sub_code = Column('business_activity_sub_code', String(140))
#    drug_schedules = Column('drug_schedules', String(140))
#    address_line_1 = Column('address_line_1', String(140))
#    address_line_2 = Column('address_line_2', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    phone_number = Column('phone_number', String(140))
#    fax_number = Column('fax_number', String(140))
#    credentials = Column('credentials', String(140))
#    practitioner_type = Column('practitioner_type', String(140))
#    federal_tax_id_number = Column('federal_tax_id_number', String(140))
#    specialty_1 = Column('specialty_1', String(140))
#    specialty_2 = Column('specialty_2', String(140))
#    state_license_1 = Column('state_license_1', String(140))
#    state_license_1_state = Column('state_license_1_state', String(140))
#    state_license_2 = Column('state_license_2', String(140))
#    state_license_2_state = Column('state_license_2_state', String(140))
#    state_license_3 = Column('state_license_3', String(140))
#    state_license_3_state = Column('state_license_3_state', String(140))
#    medicaid_id_1 = Column('medicaid_id_1', String(140))
#    medicaid_id_1_state = Column('medicaid_id_1_state', String(140))
#    medicaid_id_2 = Column('medicaid_id_2', String(140))
#    medicaid_id_2_state = Column('medicaid_id_2_state', String(140))
#    medicaid_id_3 = Column('medicaid_id_3', String(140))
#    medicaid_id_3_state = Column('medicaid_id_3_state', String(140))
#    tax_id = Column('tax_id', String(140))
#    expiration_date = Column('expiration_date', Date)
#    prescriber_id_qualifier = Column('prescriber_id_qualifier', String(140))
#    reserved = Column('reserved', String(140))
#
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#
#    def __repr__(self):
#        return self.change_enhanced_prescriber_records
#    
#class ChangeEnhancedSubmittedMemberRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_enhanced_submitted_member_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    cardholder_last_name = Column('cardholder_last_name', String(140))
#    patient_first_name = Column('patient_first_name', String(140))
#    patient_date_of_birth = Column('patient_date_of_birth', Date)
#    gender = Column('gender', String(140))
#    patient_email_address = Column('patient_email_address', String(140))
#    patient_address_street = Column('patient_address_street', String(140))
#    patient_address_city = Column('patient_address_city', String(140))
#    patient_address_state = Column('patient_address_state', String(140))
#    patient_address_zip_code = Column('patient_address_zip_code', String(140))
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_enhanced_submitted_member_records
#        
#class ChangeMultiIngredientCompoudRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_multi_ingredient_compound_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    plan = Column('plan', String(140))
#    claim_authorization_number = Column('claim_authorization_number', String(140))
#    compound_ingredient_count = Column('compound_ingredient_count', Integer)
#    drug_1_ndc_number = Column('drug_1_ndc_number', String(140))
#    drug_1_name = Column('drug_1_name', String(140))
#    drug_1_strength_description = Column('drug_1_strength_description', String(140))
#    drug_1_dose_form_description = Column('drug_1_dose_form_description', String(140))
#    drug_1_processed_sig = Column('drug_1_processed_sig', String(140))
#    drug_1_quantity = Column('drug_1_quantity', Float)
#    drug_1_plan_ingredient_cost = Column('drug_1_plan_ingredient_cost', Float)
#    drug_1_pharmacy_ingredient_cost = Column('drug_1_pharmacy_ingredient_cost', Float)
#    drug_1_covered_ingredient = Column('drug_1_covered_ingredient', Integer)
#    drug_1_formulary_indicator = Column('drug_1_formulary_indicator', Integer)
#    drug_2_ndc_number = Column('drug_2_ndc_number', String(140))
#    drug_2_name = Column('drug_2_name', String(140))
#    drug_2_strength_description = Column('drug_2_strength_description', String(140))
#    drug_2_dose_form_description = Column('drug_2_dose_form_description', String(140))
#    drug_2_processed_sig = Column('drug_2_processed_sig', String(140))
#    drug_2_quantity = Column('drug_2_quantity', Float)
#    drug_2_plan_ingredient_cost = Column('drug_2_plan_ingredient_cost', Float)
#    drug_2_pharmacy_ingredient_cost = Column('drug_2_pharmacy_ingredient_cost', Float)
#    drug_2_covered_ingredient = Column('drug_2_covered_ingredient', Integer)
#    drug_2_formulary_indicator = Column('drug_2_formulary_indicator', Integer)
#    drug_3_ndc_number = Column('drug_3_ndc_number', String(140))
#    drug_3_name = Column('drug_3_name', String(140))
#    drug_3_strength_description = Column('drug_3_strength_description', String(140))
#    drug_3_dose_form_description = Column('drug_3_dose_form_description', String(140))
#    drug_3_processed_sig = Column('drug_3_processed_sig', String(140))
#    drug_3_quantity = Column('drug_3_quantity', Float)
#    drug_3_plan_ingredient_cost = Column('drug_3_plan_ingredient_cost', Float)
#    drug_3_pharmacy_ingredient_cost = Column('drug_3_pharmacy_ingredient_cost', Float)
#    drug_3_covered_ingredient = Column('drug_3_covered_ingredient', Integer)
#    drug_3_formulary_indicator = Column('drug_3_formulary_indicator', Integer)
#    drug_4_ndc_number = Column('drug_4_ndc_number', String(140))
#    drug_4_name = Column('drug_4_name', String(140))
#    drug_4_strength_description = Column('drug_4_strength_description', String(140))
#    drug_4_dose_form_description = Column('drug_4_dose_form_description', String(140))
#    drug_4_processed_sig = Column('drug_4_processed_sig', String(140))
#    drug_4_quantity = Column('drug_4_quantity', Float)
#    drug_4_plan_ingredient_cost = Column('drug_4_plan_ingredient_cost', Float)
#    drug_4_pharmacy_ingredient_cost = Column('drug_4_pharmacy_ingredient_cost', Float)
#    drug_4_covered_ingredient = Column('drug_4_covered_ingredient', Integer)
#    drug_4_formulary_indicator = Column('drug_4_formulary_indicator', Integer)
#    drug_5_ndc_number = Column('drug_5_ndc_number', String(140))
#    drug_5_name = Column('drug_5_name', String(140))
#    drug_5_strength_description = Column('drug_5_strength_description', String(140))
#    drug_5_dose_form_description = Column('drug_5_dose_form_description', String(140))
#    drug_5_processed_sig = Column('drug_5_processed_sig', String(140))
#    drug_5_quantity = Column('drug_5_quantity', Float)
#    drug_5_plan_ingredient_cost = Column('drug_5_plan_ingredient_cost', Float)
#    drug_5_pharmacy_ingredient_cost = Column('drug_5_pharmacy_ingredient_cost', Float)
#    drug_5_covered_ingredient = Column('drug_5_covered_ingredient', Integer)
#    drug_5_formulary_indicator = Column('drug_5_formulary_indicator', Integer)
#    drug_6_ndc_number = Column('drug_6_ndc_number', String(140))
#    drug_6_name = Column('drug_6_name', String(140))
#    drug_6_strength_description = Column('drug_6_strength_description', String(140))
#    drug_6_dose_form_description = Column('drug_6_dose_form_description', String(140))
#    drug_6_processed_sig = Column('drug_6_processed_sig', String(140))
#    drug_6_quantity = Column('drug_6_quantity', Float)
#    drug_6_plan_ingredient_cost = Column('drug_6_plan_ingredient_cost', Float)
#    drug_6_pharmacy_ingredient_cost = Column('drug_6_pharmacy_ingredient_cost', Float)
#    drug_6_covered_ingredient = Column('drug_6_covered_ingredient', Integer)
#    drug_6_formulary_indicator = Column('drug_6_formulary_indicator', Integer)
#    drug_7_ndc_number = Column('drug_7_ndc_number', String(140))
#    drug_7_name = Column('drug_7_name', String(140))
#    drug_7_strength_description = Column('drug_7_strength_description', String(140))
#    drug_7_dose_form_description = Column('drug_7_dose_form_description', String(140))
#    drug_7_processed_sig = Column('drug_7_processed_sig', String(140))
#    drug_7_quantity = Column('drug_7_quantity', Float)
#    drug_7_plan_ingredient_cost = Column('drug_7_plan_ingredient_cost', Float)
#    drug_7_pharmacy_ingredient_cost = Column('drug_7_pharmacy_ingredient_cost', Float)
#    drug_7_covered_ingredient = Column('drug_7_covered_ingredient', Integer)
#    drug_7_formulary_indicator = Column('drug_7_formulary_indicator', Integer)
#    drug_8_ndc_number = Column('drug_8_ndc_number', String(140))
#    drug_8_name = Column('drug_8_name', String(140))
#    drug_8_strength_description = Column('drug_8_strength_description', String(140))
#    drug_8_dose_form_description = Column('drug_8_dose_form_description', String(140))
#    drug_8_processed_sig = Column('drug_8_processed_sig', String(140))
#    drug_8_quantity = Column('drug_8_quantity', Float)
#    drug_8_plan_ingredient_cost = Column('drug_8_plan_ingredient_cost', Float)
#    drug_8_pharmacy_ingredient_cost = Column('drug_8_pharmacy_ingredient_cost', Float)
#    drug_8_covered_ingredient = Column('drug_8_covered_ingredient', Integer)
#    drug_8_formulary_indicator = Column('drug_8_formulary_indicator', Integer)
#    drug_9_ndc_number = Column('drug_9_ndc_number', String(140))
#    drug_9_name = Column('drug_9_name', String(140))
#    drug_9_strength_description = Column('drug_9_strength_description', String(140))
#    drug_9_dose_form_description = Column('drug_9_dose_form_description', String(140))
#    drug_9_processed_sig = Column('drug_9_processed_sig', String(140))
#    drug_9_quantity = Column('drug_9_quantity', Float)
#    drug_9_plan_ingredient_cost = Column('drug_9_plan_ingredient_cost', Float)
#    drug_9_pharmacy_ingredient_cost = Column('drug_9_pharmacy_ingredient_cost', Float)
#    drug_9_covered_ingredient = Column('drug_9_covered_ingredient', Integer)
#    drug_9_formulary_indicator = Column('drug_9_formulary_indicator', Integer)
#    reserved = Column('reserved', String(140))
#    submitted_level_of_effort_code = Column('submitted_level_of_effort_code', String(140))
#    
#    def __repr__(self):
#        return self.change_multi_ingredient_compound_records
#        
#class ChangePaperClaimInfoRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_paper_claim_info_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    user_id = Column('user_id', String(140))
#    terminal_id = Column('terminal_id', String(140))
#    received_date_1 = Column('received_date_1', Date)
#    received_date_2 = Column('received_date_2', Date)
#    reference_code = Column('reference_code', String(140))
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_paper_claim_info_records
#        
#class ChangePatientInfoRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_patient_info_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    cardholder_last_name = Column('cardholder_last_name', String(140))
#    cardholder_first_name = Column('cardholder_first_name', String(140))
#    patient_middle_initial = Column('patient_middle_initial', String(140))
#    patient_name_suffix = Column('patient_name_suffix', String(140))
#    address_line_1 = Column('address_line_1', String(140))
#    address_line_2 = Column('address_line_2', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    phone_number = Column('phone_number', String(140))
#    effective_date = Column('effective_date', Date)
#    termination_date = Column('termination_date', Date)
#    date_of_birth = Column('date_of_birth', Date)
#    gender_code = Column('gender_code', Integer)
#    relationship_code = Column('relationship_code', Integer)
#    coverage_code = Column('coverage_code', Integer)
#    reserved_1 = Column('reserved_1', Integer)
#    student_flag = Column('student_flag', Integer)
#    reserved_2 = Column('reserved_2', Integer)
#    location_code = Column('location_code', String(140))
#    location_name = Column('location_name', String(140))
#    secondary_coverage = Column('secondary_coverage', Integer)
#    pharmacy_lock_in = Column('pharmacy_lock_in', Integer)
#    physician_lock_in = Column('physician_lock_in', Integer)
#    test_member_flag = Column('test_member_flag', Integer)
#    eligibility_created_by_user_id = Column('eligibility_created_by_user_id', String(140))
#    eligibility_created_date = Column('eligibility_created_date', Date)
#    reserved_3 = Column('reserved_3', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_patient_info_records
#        
#class ChangePatitentPayRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_patient_pay_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    amount_attributed_to_processor_fee = Column('amount_attributed_to_processor_fee', Float)
#    amount_of_coinsurance = Column('amount_of_coinsurance', Float)
#    reserved_1 = Column('reserved_1', String(140))
#    reserved_pricing_1 = Column('reserved_pricing_1', Float)
#    reserved_pricing_2 = Column('reserved_pricing_2', Float)
#    amount_attributed_to_brand_drug = Column('amount_attributed_to_brand_drug', Float)
#    amount_attributed_to_nonpreferred_formulary_selection = Column('amount_attributed_to_nonpreferred_formulary_selection', Float)
#    amount_attributed_to_brand_nonpreferred_formulary_selection = Column('amount_attributed_to_brand_nonpreferred_formulary_selection', Float)
#    reserved_pricing_3 = Column('reserved_pricing_3', Float)
#    reserved_pricing_4 = Column('reserved_pricing_4', Float)
#    amount_attributed_to_sales_tax = Column('amount_attributed_to_sales_tax', Float)
#    reserved_2 = Column('reserved_2', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_patient_pay_records
#        
#class ChangePharmacyPricingRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_pharmacy_pricing_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    pharmacy_ingredient_cost = Column('pharmacy_ingredient_cost', Float)
#    pharmacy_dispensing_fee = Column('pharmacy_dispensing_fee', Float)
#    pharmacy_sales_tax = Column('pharmacy_sales_tax', Float)
#    pharmacy_gross_amount = Column('pharmacy_gross_amount', Float)
#    pharmacy_copay_amount = Column('pharmacy_copay_amount', Float)
#    pharmacy_due_amount = Column('pharmacy_due_amount', Float)
#    pharmacy_basis_of_cost = Column('pharmacy_basis_of_cost', String(140))
#    pharmacy_basis_of_reimbursement = Column('pharmacy_basis_of_reimbursement', Integer)
#    pharmacy_calculated_amount = Column('pharmacy_calculated_amount', Float)
#    processor_fee = Column('processor_fee', Float)
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_pharmacy_pricing_records
#        
#class ChangePharmacyRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_pharmacy_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    address_line_1 = Column('address_line_1', String(140))
#    address_line_2 = Column('address_line_2', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    phone_number = Column('phone_number', String(140))
#    reserved_1 = Column('reserved_1', String(140))
#    fax_number = Column('fax_number', String(140))
#    federal_license_number = Column('federal_license_number', String(140))
#    federal_tax_id_number = Column('federal_tax_id_number', String(140))
#    state_license_number = Column('state_license_number', String(140))
#    state_tax_id_number = Column('state_tax_id_number', String(140))
#    state_tax_medicaid_number = Column('state_tax_medicaid_number', String(140))
#    pharmacy_store_number = Column('pharmacy_store_number', String(140))
#    test_pharmacy_flag = Column('test_pharmacy_flag', String(140))
#    pharmacist_id_qualifier = Column('pharmacist_id_qualifier', String(140))
#    pharmacist_id = Column('pharmacist_id', String(140))
#    primary_pharmacy_dispenser_type = Column('primary_pharmacy_dispenser_type', String(140))
#    reserved_2 = Column('reserved_2', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    
#    def __repr__(self):
#        return self.change_pharmacy_records
#        
#class ChangePlanCodesUsedRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_plan_codes_used_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    line_of_business_code = Column('line_of_business_code', String(140))
#    plan_network_code = Column('plan_network_code', String(140))
#    margin_network_code = Column('margin_network_code', String(140))
#    common_formulary_code = Column('common_formulary_code', String(140))
#    plan_formulary_code = Column('plan_formulary_code', String(140))
#    pharmacy_formulary_code = Column('pharmacy_formulary_code', String(140))
#    common_mac_code = Column('common_mac_code', String(140))
#    copay_code = Column('copay_code', String(140))
#    level_2_messaging_code = Column('level_2_messaging_code', String(140))
#    member_plan_code = Column('member_plan_code', String(140))
#    plan_common_mac_code = Column('plan_common_mac_code', String(140))
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    def __repr__(self):
#        return self.change_plan_codes_used_records
#        
#class ChangePriorAuthorizationRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_prior_authorization_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    pa_type_submitted = Column('pa_type_submitted', Integer)
#    pa_number_submitted = Column('pa_number_submitted', Integer)
#    actual_pa_number_used = Column('actual_pa_number_used', Integer)
#    pa_type = Column('pa_type', String(140))
#    pa_effective_date = Column('pa_effective_date', Date)
#    pa_termination_date = Column('pa_termination_date', Date)
#    pa_description = Column('pa_description', String(140))
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    def __repr__(self):
#        return self.change_prior_authorization_records
#        
#class ChangeSubmittedCobClaimInfoRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_submitted_cob_claim_info_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    coordination_of_benefits_other_payments_count = Column('coordination_of_benefits_other_payments_count', String(140))
#    other_payer_coverage_type_primary = Column('other_payer_coverage_type_primary', String(140))
#    other_payer_id_qualifier_primary = Column('other_payer_id_qualifier_primary', String(140))
#    other_payer_id_bin_primary = Column('other_payer_id_bin_primary', String(140))
#    other_payer_date_primary = Column('other_payer_date_primary', Date)
#    reject_count_primary = Column('reject_count_primary', Integer)
#    reject_code_1_primary = Column('reject_code_1_primary', String(140))
#    reject_code_2_primary = Column('reject_code_2_primary', String(140))
#    reject_code_3_primary = Column('reject_code_3_primary', String(140))
#    other_payer_patient_responsibility_amount_qualifier_primary = Column('other_payer_patient_responsibility_amount_qualifier_primary', String(140))
#    other_payer_patient_responsibility_amount_sum_primary = Column('other_payer_patient_responsibility_amount_sum_primary', Integer)
#    other_payer_amount_paid_sum_primary = Column('other_payer_amount_paid_sum_primary', Integer)
#    other_payer_coverage_type_secondary = Column('other_payer_coverage_type_secondary', String(140))
#    other_payer_id_qualifier_secondary = Column('other_payer_id_qualifier_secondary', String(140))
#    other_payer_id_bin_secondary = Column('other_payer_id_bin_secondary', String(140))
#    other_payer_date_secondary = Column('other_payer_date_secondary', Date)
#    reject_count_secondary = Column('reject_count_secondary', Integer)
#    reject_code_1_secondary = Column('reject_code_1_secondary', String(140))
#    reject_code_2_secondary = Column('reject_code_2_secondary', String(140))
#    reject_code_3_secondary = Column('reject_code_3_secondary', String(140))
#    other_payer_patient_responsibility_amount_qualifier_secondary = Column('other_payer_patient_responsibility_amount_qualifier_secondary', String(140))
#    other_payer_patient_responsibility_amount_sum_secondary = Column('other_payer_patient_responsibility_amount_sum_secondary', Integer)
#    other_payer_amount_paid_sum_secondary = Column('other_payer_amount_paid_sum_secondary', Integer)
#    other_payer_coverage_type_tertiary = Column('other_payer_coverage_type_tertiary', String(140))
#    other_payer_id_qualifier_tertiary = Column('other_payer_id_qualifier_tertiary', String(140))
#    other_payer_id_bin_tertiary = Column('other_payer_id_bin_tertiary', String(140))
#    other_payer_date_tertiary = Column('other_payer_date_tertiary', Date)
#    reject_count_tertiary = Column('reject_count_tertiary', Integer)
#    reject_code_1_tertiary = Column('reject_code_1_tertiary', String(140))
#    reject_code_2_tertiary = Column('reject_code_2_tertiary', String(140))
#    reject_code_3_tertiary = Column('reject_code_3_tertiary', String(140))
#    other_payer_patient_responsibility_amount_qualifier_tertiary = Column('other_payer_patient_responsibility_amount_qualifier_tertiary', String(140))
#    other_payer_patient_responsibility_amount_sum_tertiary = Column('other_payer_patient_responsibility_amount_sum_tertiary', Integer)
#    other_payer_amount_paid_sum_tertiary = Column('other_payer_amount_paid_sum_tertiary', Integer)
#    other_payer_bin_name_primary = Column('other_payer_bin_name_primary', String(140))
#    other_payer_bin_name_secondary = Column('other_payer_bin_name_secondary', String(140))
#    other_payer_bin_name_tertiary = Column('other_payer_bin_name_tertiary', String(140))
#    benefit_stage_information_presented_primary = Column('benefit_stage_information_presented_primary', String(140))
#    benefit_stage_information_presented_secondary = Column('benefit_stage_information_presented_secondary', String(140))
#    benefit_stage_information_presented_tertiary = Column('benefit_stage_information_presented_tertiary', String(140))
#    reserved = Column('reserved', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    def __repr__(self):
#        return self.change_submitted_cob_claim_info_records
#        
#class ChangeSubmittedDurOverrideRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'change_submitted_dur_override_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #change_claim_record_id = Column('change_claim_record_id', Integer)
#    reason_for_service_1 = Column('reason_for_service_1', String(140))
#    professional_service_code_1 = Column('professional_service_code_1', String(140))
#    result_of_service_code_1 = Column('result_of_service_code_1', String(140))
#    reason_for_service_2 = Column('reason_for_service_2', String(140))
#    professional_service_code_2 = Column('professional_service_code_2', String(140))
#    result_of_service_code_2 = Column('result_of_service_code_2', String(140))
#    reason_for_service_3 = Column('reason_for_service_3', String(140))
#    professional_service_code_3 = Column('professional_service_code_3', String(140))
#    result_of_service_code_3 = Column('result_of_service_code_3', String(140))
#    reason_for_service_4 = Column('reason_for_service_4', String(140))
#    professional_service_code_4 = Column('professional_service_code_4', String(140))
#    result_of_service_code_4 = Column('result_of_service_code_4', String(140))
#    reason_for_service_5 = Column('reason_for_service_5', String(140))
#    professional_service_code_5 = Column('professional_service_code_5', String(140))
#    result_of_service_code_5 = Column('result_of_service_code_5', String(140))
#    
#    change_claim_record_id = Column('change_claim_record_id', Integer, ForeignKey("change_claim_records.id"), nullable=False)
#    change_claim_records = relationship("ChangeClaimRecords")
#
#    def __repr__(self):
#        return self.change_submitted_dur_override_records
#        
#class Companies(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'companies'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    name = Column('name', String(140))
#    enable_app_access = Column('enable_app_access', Boolean)
#    enable_wallet_card = Column('enable_wallet_card', Boolean)
#    phone = Column('phone', String(140))
#    #address_id = Column('address_id', Integer)
#    calendar_id = Column('calendar_id', String(140))
#    
#    address_id = Column('address_id', Integer, ForeignKey("addresses.id"), nullable=False)
#    addresses = relationship("Addresses")
#
#    def __repr__(self):
#        return self.companies
#        
#class CompanyLocations(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'company_locations'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #company_id = Column('company_id', Integer)
#    #address_id = Column('address_id', Integer)
#    name = Column('name', String(140))
#    store_number = Column('store_number', String(140))
#    phone = Column('phone', String(140))
#    
#    company_id = Column('company_id', Integer, ForeignKey("companies.id"), nullable=False)
#    companies = relationship("Companies")
#
#    address_id = Column('address_id', Integer, ForeignKey("addresses.id"), nullable=False)
#    addresses = relationship("Addresses")
#
#    def __repr__(self):
#        return self.company_locations
#        
#class CompanyUsers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'company_users'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #company_id = Column('company_id', Integer)
#    #user_id = Column('user_id', Integer)
#    guid = Column('guid', String(140))
#    #company_location_id = Column('company_location_id', Integer)
#    covid_risk_category = Column('covid_risk_category', String(140))
#    
#    company_id = Column('company_id', Integer, ForeignKey("companies.id"), nullable=False)
#    companies = relationship("Companies")
#
#    user_id = Column('user_id', Integer, ForeignKey("users.id"), nullable=False)
#    users = relationship("Users")
#    
#    company_location_id = Column('company_location_id', Integer, ForeignKey("company_locations.id"), nullable=False)
#    company_locations = relationship('CompanyLocations')
#
#    def __repr__(self):
#        return self.company_users
# 
#class Entities(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'entities'
#
#    entity_id = Column('entity_id', Integer, primary_key=True, autoincrement=True)
#    
#    entity_name_id = Column('entity_name_id', Integer, ForeignKey("entity_name.entity_name_id"), nullable=False)
#    entity_name = relationship('EntityName')
#    
#    entity_department_id = Column('entity_department_id', Integer, ForeignKey("entity_department.entity_department_id"), nullable=False)
#    entity_department = relationship("EntityDepartment")
# 
#    def __repr__(self):
#        return self.entities
#        
#class EntityName(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'entity_name'
#    
#    entity_name_id = Column('entity_name_id', Integer, primary_key=True, autoincrement=True)
#    entity_name = Column('entity_name', String(140))
#    phone = Column('phone', String(140))
#    fax = Column('fax', String(140))
#    npi = Column('npi', String(140))
#    
#    address_id = Column('address_id', Integer, ForeignKey("addresses.address_id"), nullable=False)
#    addresses = relationship('Addresses')
#
#    def __repr__(self):
#        return self.entity_name
#        
#class EntityDepartment(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'entity_department'
#    
#    entity_department_id = Column('entity_department_id', Integer, primary_key=True, autoincrement=True)
#    entity_department = Column('entity_department', String(140))
#    
#    def __repr__(self):
#        return self.entity_department
#        
#        
# 
#class DashboardItems(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'dashboard_items'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    category = Column('category', String(140))
#    title  = Column('title', String(140))
#    url = Column('url', String(140))
#    image_url = Column('image_url', String(140))
#    
#    def __repr__(self):
#        return self.dashboard_items
#        
#class Doctors(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'doctors'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    first_name = Column('first_name', String(140))
#    last_name = Column('last_name', String(140))
#    specialty = Column('specialty', String(140))
#    address = Column('address', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    phone = Column('phone', String(140))
#    fax = Column('fax', String(140))
#    npi = Column('npi', String(140))
#    dea = Column('dea', String(140))
#    state_license = Column('state_license', String(140))
#    supervisor = Column('supervisor', String(140))
#    
#    def __repr__(self):
#        return self.doctors
#        
#class EprescriptionChangeRequests(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'eprescription_change_requests'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #eprescription_id = Column('eprescription_id', Integer)
#    request_code = Column('request_code', String(140))
#    request_notes = Column('request_notes', String(140))
#    medication_requested = Column('medication_requested', JSON)
#    #response_message_id = Column('response_message_id', Integer)
#    response = Column('response', String(140))
#    response_notes = Column('response_notes', String(140))
#    
#    response_message_id = Column('response_message_id', Integer, ForeignKey("surescripts_messages.id"), nullable=False)
#    surescripts_messages = relationship("SurescriptsMessages")
#    
#    eprescription_id = Column('eprescription_id', Integer, ForeignKey("eprescriptions.id"), nullable=False)
#    eprescriptions = relationship("Eprescriptions")
#
#    def __repr__(self):
#        return self.eprescription_change_requests
#        
#class EprescriptionFills(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'eprescription_fills'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #eprescription_id = Column('eprescription_id', Integer)
#    quantity = Column('quantity', Float)
#    
#    eprescription_id = Column('eprescription_id', Integer, ForeignKey("eprescriptions.id"), nullable=False)
#    eprescriptions = relationship("Eprescriptions")    
#    
#    def __repr__(self):
#        return self.eprescription_fills
#        
#class EprescriptionRenewalRequests(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'eprescription_renewal_requests'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #eprescription_id = Column('eprescription_id', Integer)
#    refills_requested = Column('refills_requested', Integer)
#    #response_message_id = Column('response_message_id', Integer)
#    response = Column('response', String(140))
#    response_notes = Column('response_notes', String(140))
#    
#    response_message_id = Column('response_message_id', Integer, ForeignKey("surescripts_messages.id"), nullable=False)
#    surescripts_messages = relationship("SurescriptsMessages")
#    
#    eprescription_id = Column('eprescription_id', Integer, ForeignKey("eprescriptions.id"), nullable=False)
#    eprescriptions = relationship("Eprescriptions")
#
#    def __repr__(self):
#        return self.eprescription_renewal_requests
#        
#class Eprescriptions(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'eprescriptions'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #prescriber_id = Column('prescriber_id', Integer)
#    supervisor_id = Column('supervisor_id', Integer)
#    #user_id = Column('user_id', Integer)
#    patient_first_name = Column('patient_first_name', String(140))
#    patient_middle_name = Column('patient_middle_name', String(140))
#    patient_last_name = Column('patient_last_name', String(140))
#    patient_suffix = Column('patient_suffix', String(140))
#    patient_sex = Column('patient_sex', String(140))
#    patient_date_of_birth = Column('patient_date_of_birth', Date)
#    patient_phone = Column('patient_phone', String(140))
#    patient_phone_sms_enabled = Column('patient_phone_sms_enabled', Boolean)
#    patient_email = Column('patient_email', String(140))
#    patient_address_id = Column('patient_address_id', Integer)
#    state = Column('state', String(140))
#    prescriber_order_number = Column('prescriber_order_number', String(140))
#    ndc = Column('ndc', String(140))
#    name = Column('name', String(140))
#    description = Column('description', String(140))
#    dea_schedule_code = Column('dea_schedule_code', String(140))
#    strength = Column('strength', String(140))
#    strength_uom_code = Column('strength_uom_code', String(140))
#    strength_uom = Column('strength_uom', String(140))
#    quantity = Column('quantity', Float)
#    quantity_uom_code = Column('quantity_uom_code', String(140))
#    quantity_uom = Column('quantity_uom', String(140))
#    days_supply = Column('days_supply', Integer)
#    substitutions = Column('substitutions', Integer)
#    number_of_refills = Column('number_of_refills', Integer)
#    sig_text = Column('sig_text', String(140))
#    dosage_method = Column('dosage_method', String(140))
#    dosage_quantity = Column('dosage_quantity', Float)
#    dosage_quantity_uom = Column('dosage_quantity_uom', String(140))
#    dosage_route_of_administration = Column('dosage_route_of_administration', String(140))
#    dosage_frequency = Column('dosage_frequency', Integer)
#    dosage_frequency_uom = Column('dosage_frequency_uom', String(140))
#    dosage_frequency_text = Column('dosage_frequency_text', String(140))
#    written_at = Column('written_at', DateTime)
#    notes = Column('notes', String(140))
#    prior_authorization = Column('prior_authorization', String(140))
#    canceled_at = Column('canceled_at', DateTime)
#    dispensed_at = Column('dispensed_at', DateTime)
#    transferred_at = Column('transferred_at', DateTime)
#    filled_at = Column('filled_at', DateTime)
#    reversed_at = Column('reversed_at', DateTime)
#    prior_authorization_status_code = Column('prior_authorization_status_code', String(140))
#    generic_ndc = Column('generic_ndc', String(140))
#    generic_name = Column('generic_name', String(140))
#    #pharmacy_id = Column('pharmacy_id', Integer)
#    transfer_price = Column('transfer_price', Float)
#    claim_number = Column('claim_number', String(140))
#    reversal_number = Column('reversal_number', String(140))
#    
##    prescriber_id = Column('prescriber_id', Integer, ForeignKey("prescribers.id"), nullable=False)
##    prescribers = relationship("Prescribers")
#    
#    user_id = Column('user_id', Integer, ForeignKey("users.id"), nullable=False)
#    users = relationship("Users")
#    
#    location_id = Column('location_id', Integer, ForeignKey("locations.id"), nullable=False)
#    locations = relationship("Locations")
#    
#    def __repr__(self):
#        return self.eprescriptions
        
#class FileImportLogs(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'file_import_logs'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    vendor = Column('vendor', String(140))
#    file_type = Column('file_type', String(140))
#    filename = Column('filename', String(140))
#    
#    def __repr__(self):
#        return self.file_import_logs
#        
#class HipaaWaivers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'hipaa_waivers'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    lab_test_group_name = Column('lab_test_group_name', String(140))
#    expires_on = Column('expires_on', Date)
#    signature_data = Column('signature_data', JSON)
#    #company_user_id = Column('company_user_id', Integer)
#    
#    company_user_id = Column('company_user_id', Integer, ForeignKey("company_users.id"), nullable=False)
#    company_users = relationship("CompanyUsers")
#
#    def __repr__(self):
#        return self.hipaa_waivers
#        
#class ImaAccumulatorRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'ima_accumulator_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    carrier = Column('carrier', String(140))
#    group = Column('group', String(140))
#    subscriber_id = Column('subscriber_id', String(140))
#    dependent_number = Column('dependent_number', Integer)
#    adjustment_date = Column('adjustment_date', Date)
#    accumulator_type = Column('accumulator_type', String(140))
#    adjustment_amount = Column('adjustment_amount', Float)
#    date_of_birth = Column('date_of_birth', Date)
#    last_name = Column('last_name', String(140))
#    first_name = Column('first_name', String(140))
#    processed_at = Column('processed_at', Date)
#    
#    def __repr__(self):
#        return self.ima_accumulator_records
#        
#class ImaEligibilityRecords(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'ima_eligibility_records'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    client_field = Column('client_field', String(140))
#    subscriber_id = Column('subscriber_id', String(140))
#    subscriber_ssn = Column('subscriber_ssn', String(140))
#    group = Column('group', String(140))
#    enrollment_level = Column('enrollment_level', String(140))
#    last_name = Column('last_name', String(140))
#    first_name = Column('first_name', String(140))
#    middle_initial = Column('middle_initial', String(140))
#    date_of_birth = Column('date_of_birth', Date)
#    sex = Column('sex', String(140))
#    relation_code = Column('relation_code', Integer)
#    effective_date = Column('effective_date', Date)
#    termination_date = Column('termination_date', Date)
#    cobra = Column('cobra', Boolean)
#    record_type = Column('record_type', String(140))
#    dependent_number = Column('dependent_number', Integer)
#    division = Column('division', String(140))
#    street1 = Column('street1', String(140))
#    street2 = Column('street2', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    file_created_at = Column('file_created_at', Date)
#    processed_at = Column('processed_at', Date)
#    
#    def __repr__(self):
#        return self.ima_eligibility_records
#        
#class InsuranceProviders(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'insurance_providers'
#    
#    insurance_provider_id = Column('insurance_provider_id', Integer, primary_key=True, autoincrement=True)
#    name = Column('name', String(140))
#    trading_partner_id = Column('trading_partner_id', String(140))
#    
#    def __repr__(self):
#        return self.insurance_providers
#        
#class Insurances(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'insurances'
#    
#    insurance_id = Column('insurance_id', Integer, primary_key=True, autoincrement=True)
#    #user_id = Column('user_id', Integer)
#    #insurance_provider_id = Column('insurance_provider_id', Integer)
#    rx_bin = Column('rx_bin', String(140))
#    rx_pcn = Column('rx_pcn', String(140))
#    rx_group = Column('rx_group', String(140))
#    member_id = Column('member_id', String(140))
#    eligibility_response = Column('eligibility_response', JSON)
#    
#
#
#    insurance_provider_id = Column('insurance_provider_id', Integer, ForeignKey("insurance_providers.insurance_provider_id"), nullable=False)
#    insurance_providers = relationship("InsuranceProviders")
#
#    def __repr__(self):
#        return self.insurances
#        
#    
#class LabTestOrders(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'lab_test_orders'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #lab_test_id = Column('lab_test_id', Integer)
#    #company_user_id = Column('company_user_id', Integer)
#    vendor_order_number = Column('vendor_order_number', String(140))
#    results = Column('results', String(140))
#    guid = Column('guid', String(140))
#    appointment_id = Column('appointment_id', String(140))
#    scheduled_for = Column('scheduled_for', DateTime)
#    vendor_batch_number = Column('vendor_batch_number', String(140))
#    submitted_to_vendor_at = Column('submitted_to_vendor_at', DateTime)
#    #doctor_id = Column('doctor_id', Integer)
#    
#    doctor_id = Column('doctor_id', Integer, ForeignKey("doctors.id"), nullable=False)
#    doctors = relationship("Doctors")
#
#    lab_test_id = Column('lab_test_id', Integer, ForeignKey("lab_tests.id"), nullable=False)
#    lab_tests = relationship("LabTests")
#
#    company_user_id = Column('company_user_id', Integer, ForeignKey("company_users.id"), nullable=False)
#    company_users = relationship("CompanyUsers")
#
#    def __repr__(self):
#        return self.lab_test_orders
#        
#class LabTests(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'lab_tests'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    name = Column('name', String(140))
#    description = Column('description', String(140))
#    vendor_name = Column('vendor_name', String(140))
#    vendor_test_number = Column('vendor_test_number', String(140))
#    group_name = Column('group_name', String(140))
#    category = Column('category', String(140))
#    
#    def __repr__(self):
#        return self.lab_tests
#        
#class LabcorpBulkResultsOrder(Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'labcorp_bulk_results_order'
#    
#    lab = Column('lab', String(140))
#    specimen_number = Column('specimen_number', String(140))
#    account_number = Column('account_number', String(140))
#    requisition_control_number = Column('requisition_control_number', String(140))
#    external_patient_id = Column('external_patient_id', String(140))
#    patient_gender = Column('patient_gender', String(140))
#    patient_birth = Column('patient_birth', String(140))
#    patient_last_name = Column('patient_last_name', String(140))
#    patient_first_name = Column('patient_first_name', String(140))
#    patient_address = Column('patient_address', String(140))
#    patient_city = Column('patient_city', String(140))
#    patient_state = Column('patient_state', String(140))
#    patient_zip_code = Column('patient_zip_code', String(140))
#    patient_phone_number = Column('patient_phone_number', String(140))
#    relevant_clinical_information = Column('relevant_clinical_information', String(140))
#    collection_date = Column('collection_date', String(140))
#    date_observation = Column('date_observation', String(140))
#    test_number = Column('test_number', String(140))
#    test_name = Column('test_name', String(140))
#    result_status = Column('result_status', String(140))
#    results = Column('results', String(140))
#    comments = Column('comments', String(140))
#    facility_mnemonic = Column('facility_mnemonic', String(140))
#    facility_name = Column('facility_name', String(140))
#    facility_address = Column('facility_address', String(140))
#    facility_city = Column('facility_city', String(140))
#    facility_state = Column('facility_state', String(140))
#    facility_zip_code = Column('facility_zip_code', String(140))
#    doctor_phone_number = Column('doctor_phone_number', String(140))
#    doctor_title = Column('doctor_title', String(140))
#    doctor_last_name = Column('doctor_last_name', String(140))
#    doctor_first_name = Column('doctor_first_name', String(140))
#    doctor_degree = Column('doctor_degree', String(140))
#    created_at = Column('created_at', String(140))
#    uuid = Column('uuid', String(140))
#    file_name = Column('file_name', String(140))
#    
#    def __repr__(self):
#        return self.labcorp_bulk_results_order
#        
#class LabcorpHl7Results(Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'labcorp_hl7_results'
#    
#    dfsaddress = Column('dfsaddress', String(140))
#    source = Column('source', String(140))
#    dfsdate = Column('dfsdate', String(140))
#    dfsid = Column('dfsid', String(140))
#    dfsname = Column('dfsname', String(140))
#    dfsegmentsfc = Column('dfsegmentsfc', String(140))
#    dfsegmentsrep = Column('dfsegmentsrep', String(140))
#    dfsegmentsseq = Column('dfsegmentsseq', String(140))
#    dfsegmentsvf = Column('dfsegmentsvf', String(140))
#    dfsegmentsval = Column('dfsegmentsval', String(140))
#    dfsegmentsid = Column('dfsegmentsid', String(140))
#    dfsegmentsfieldsval = Column('dfsegmentsfieldsval', String(140))
#    dfsegmentsfieldsid = Column('dfsegmentsfieldsid', String(140))
#    processed_at = Column('processed_at', DateTime)
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    
#    def __repr__(self):
#        return self.labcorp_hl7_results
#        
#class LabcorpOrderDetails(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'labcorp_order_details'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #lab_test_order_id = Column('lab_test_order_id', Integer)
#    data = Column('data', JSON)
#    alternative_control_number = Column('alternative_control_number', String(140))
#    specimen_number = Column('specimen_number', String(140))
#    collected_at = Column('collected_at', DateTime)
#    reported_at = Column('reported_at', DateTime)
#    clinical_info = Column('clinical_info', String(140))
#    is_fasting = Column('is_fasting', Boolean)
#    collection_volume = Column('collection_volume', String(140))
#    specimen_source = Column('specimen_source', String(140))
#    abnormal_flag = Column('abnormal_flag', String(140))
#    collection_units = Column('collection_units', String(140))
#    reference_range = Column('reference_range', String(140))
#    test_status = Column('test_status', String(140))
#    lab_site = Column('lab_site', String(140))
#    provider_npi = Column('provider_npi', String(140))
#    ordering_provider = Column('ordering_provider', String(140))
#    observation_notes = Column('observation_notes', String(140))
#    patient_notes = Column('patient_notes', String(140))
#    specimen_status = Column('specimen_status', String(140))
#    ordering_provider_first_name = Column('ordering_provider_first_name', String(140))
#    ordering_provider_last_name = Column('ordering_provider_last_name', String(140))
#    facility_street = Column('facility_street', String(140))
#    facility_city = Column('facility_city', String(140))
#    facility_state = Column('facility_state', String(140))
#    facility_zip_code = Column('facility_zip_code', String(140))
#    facility_phone = Column('facility_phone', String(140))
#    facility_director_prefix = Column('facility_director_prefix', String(140))
#    facility_director_first_name = Column('facility_director_first_name', String(140))
#    facility_director_middle_name = Column('facility_director_middle_name', String(140))
#    facility_director_last_name = Column('facility_director_last_name', String(140))
#    
#    lab_test_order_id = Column('lab_test_order_id', Integer, ForeignKey("lab_test_orders.id"), nullable=False)
#    lab_test_orders = relationship("LabTestOrders")
#
#    def __repr__(self):
#        return self.labcorp_order_details
#        
#class NcpdpTerminologies(Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'ncpdp_terminologies'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    ncit_subset_code = Column('ncit_subset_code', String(140))
#    ncpdp_subset_preferred_term = Column('ncpdp_subset_preferred_term', String(140))
#    ncit_code = Column('ncit_code', String(140))
#    ncpdp_preferred_term = Column('ncpdp_preferred_term', String(140))
#    ncpdp_synonym = Column('ncpdp_synonym', String(140))
#    ncit_preferred_term = Column('ncit_preferred_term', String(140))
#    ncit_definition = Column('ncit_definition', String(140))
#    
#    def __repr__(self):
#        return self.ncpdp_terminologies
#        
#class Pharmacies(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'pharmacies'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #address_id = Column('address_id', Integer)
#    npi = Column('npi', String(140))
#    name = Column('name', String(140))
#    phone = Column('phone', String(140))
#    price = Column('price', Float)
#    fax = Column('fax', String(140))
#    
#    address_id = Column('address_id', Integer, ForeignKey("addresses.id"), nullable=False)
#    addresses = relationship("Addresses")
#
#    def __repr__(self):
#        return self.pharmacies
#        
#        
#class Prescribers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'prescribers'
#    
#    prescriber_id = Column('prescriber_id', Integer, primary_key=True, autoincrement=True)
#    category = Column('category', String(140))
#    npi = Column('npi', String(140))
#    dea_number = Column('dea_number', String(140))
#    state_license_number = Column('state_license_number', String(140))
#    first_name = Column('first_name', String(140))
#    middle_name = Column('middle_name', String(140))
#    last_name = Column('last_name', String(140))
#    suffix = Column('suffix', String(140))
#    #address_id = Column('address_id', Integer)
#    phone = Column('phone', String(140))
#    phone_extension = Column('phone_extension', String(140))
#    fax = Column('fax', String(140))
#    fax_extension= Column('fax_extension', String(140))
#    specialty_code = Column('specialty_code', String(140))
#    specialty = Column('specialty', String(140))
#  
#    #address_id = Column('address_id', Integer, ForeignKey("addresses.id"), nullable=False)
#    #addresses = relationship("Addresses")  
#    
#    
#    def __repr__(self):
#        return self.prescribers
#        
#class Prescriptions(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'prescriptions'
#    
#    prescription_id = Column('prescription_id', Integer, primary_key=True, autoincrement=True)
#    #user_id = Column('user_id', Integer)
#    #doctor_id = Column('doctor_id', Integer)
#    #pharmacy_id = Column('pharmacy_id', Integer)
#    patient_name = Column('patient_name', String(140))
#    patient_first_name = Column('patient_first_name', String(140))
#    patient_middle_name = Column('patient_middle_name', String(140))
#    patient_last_name = Column('patient_last_name', String(140))
#    patient_suffix = Column('patient_suffix', String(140))
#    patient_date_of_birth = Column('patient_date_of_birth', Date)
#    patient_sex = Column('patient_sex', String(140))
#    patient_address_street1 = Column('patient_address_street1', String(140))
#    patient_address_city = Column('patient_address_city', String(140))
#    patient_address_state = Column('patient_address_state', String(140))
#    patient_address_zip_code = Column('patient_address_zip_code', String(140))
#    patient_email = Column('patient_email', String(140))
#    patient_phone = Column('patient_phone', String(140))
#    patient_cell_phone = Column('patient_cell_phone', String(140))
#    primary_payer_person_code = Column('primary_payer_person_code', String(140))
#    refills_authorized = Column('refills_authorized', Integer)
#    refills_remaining = Column('refills_remaining', Integer)
#    rx_number = Column('rx_number', String(140))
#    new = Column('new', Boolean)
#    transferred_at = Column('transferred_at', DateTime)
#    filled_at = Column('filled_at', DateTime)
#    dispensed_at = Column('dispensed_at', DateTime)
#    canceled_at = Column('canceled_at', DateTime)
#    claim_number = Column('claim_number', String(140))
#    reversal_number = Column('reversal_number', String(140))
#    reversed_at = Column('reversed_at', DateTime)
#    written_on = Column('written_on', Date)
#    prior_authorization = Column('prior_authorization', String(140))
#    prior_authorization_status_code = Column('prior_authorization_status_code', String(140))
#    drug = Column('drug', String(140))
#    drug_name = Column('drug_name', String(140))
#    dose_form = Column('dose_form', String(140))
#    dose_strength = Column('dose_strength', String(140))
#    dosage_frequency = Column('dosage_frequency', String(140))
#    dosage_frequency_text = Column('dosage_frequency_text', String(140))
#    dosage_frequency_uom = Column('dosage_frequency_uom', String(140))
#    dosage_method = Column('dosage_method', String(140))
#    dosage_quantity = Column('dosage_quantity', Float)
#    dosage_quantity_uom = Column('dosage_quantity_uom', String(140))
#    dosage_route_of_administration = Column('dosage_route_of_administration', String(140))
#    quantity = Column('quantity', Integer)
#    quantity_uom = Column('quantity_uom', String(140))
#    quantity_uom_code = Column('quantity_uom_code', String(140))
#    strength = Column('strength', String(140))
#    strength_uom = Column('strength_uom', String(140))
#    strength_uom_code = Column('strength_uom_code', String(140))
#    substitutions = Column('substitutions', String(140))
#    name = Column('name', String(140))
#    description = Column('description', String(140))
#    ndc = Column('ndc', String(140))
#    sig = Column('sig', String(140))
#    awp = Column('awp', Float)
#    generic_ndc = Column('generic_ndc', String(140))
#    generic_drug_name = Column('generic_drug_name', String(140))
#    generic_awp = Column('generic_awp', Float)
#    transfer_price = Column('transfer_price', Float)
#    controlled_substance_class = Column('controlled_substance_class', String(140))
#    daw_code = Column('daw_code', Integer)
#    test = Column('test', Boolean)
#    notes = Column('notes', String(140))
#    days_supply = Column('days_supply', Integer)
#    prescription_type = Column('prescription_type', String(140))
#    
#    
#    user_id = Column('user_id', Integer, ForeignKey("users.user_id"), nullable=False)
#    users = relationship("Users")
#    
#    prescriber_id = Column('prescriber_id', Integer, ForeignKey("prescribers.prescriber_id"), nullable=False)
#    prescribers = relationship("Prescribers")
#    
#    entity_id = Column('entity_id', Integer, ForeignKey("entities.entity_id"), nullable=False)
#    entities = relationship("Entities")
#    
#    prescription_status_id = Column('prescription_status_id', Integer, ForeignKey("prescription_status.id"), nullable=False)
#    prescription_status = relationship("PrescriptionStatus")
#   
#
#    def __repr__(self):
#        return self.prescriptions
#        
#        
#class PrescriptionStatus(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'prescription_status'
#    
#    prescription_status_id = Column('prescription_status_id', Integer, primary_key=True, autoincrement=True)
#    prescription_status = Column('prescription_status', String(140))
#    
#    def __repr__(self):
#        return self.prescription_status
#    
#class RapidTestUsers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'rapid_test_users'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    email = Column('email', String(140))
#    encrypted_password = Column('encrypted_password', String(140))
#    sign_in_count = Column('sign_in_count', Integer)
#    current_sign_in_at = Column('current_sign_in_at', DateTime)
#    last_sign_in_at = Column('last_sign_in_at', DateTime)
#    current_sign_in_ip = Column('current_sign_in_ip', String(140))
#    last_sign_in_ip = Column('last_sign_in_ip', String(140))
#    failed_attempts = Column('failed_attempts', Integer)
#    unlock_token = Column('unlock_token', String(140))
#    locked_at = Column('locked_at', DateTime)
#    company_id = Column('company_id', Integer)
#    first_name = Column('first_name', String(140))
#    last_name = Column('last_name', String(140))
#    
#    def __repr__(self):
#        return self.rapid_test_users
#        
        
#class SurescriptsMessages(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'surescripts_messages'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    message_type = Column('message_type', String(140))
#    message_id = Column('message_id', String(140))
#    related_message_id = Column('related_message_id', String(140))
#    file_id = Column('file_id', String(140))
#    sent_at = Column('sent_at', DateTime)
#    data = Column('data', JSON)
#    #eprescription_id = Column('eprescription_id', Integer)
#    prescriber_order_number = Column('prescriber_order_number', String(140))
#    state = Column('state', String(140))
#    rx_reference_number = Column('rx_reference_number', String(140))
#    
#    prescriptions_header_id = Column('prescriptions_header_id', Integer, ForeignKey("prescriptions_header.id"), nullable=False)
#    prescriptions_header = relationship("PrescriptionsHeader")
#
#    def __repr__(self):
#        return self.surescripts_messages
#        
#class SurescriptsOrganizations(Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'surescripts_organizations'
#    
#    organization_id = Column('organization_id', Integer, primary_key=True, autoincrement=True)
#    ncpdp = Column('ncpdp', String(140))
#    store_number = Column('store_number', String(140))
#    organization_name = Column('organization_name', String(140))
#    address_line_1 = Column('address_line_1', String(140))
#    address_line_2 = Column('address_line_2', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    country_code = Column('country_code', String(140))
#    standardized_address_line_1 = Column('standardized_address_line_1', String(140))
#    standardized_address_line_2 = Column('standardized_address_line_2', String(140))
#    standardized_city = Column('standardized_city', String(140))
#    standardized_state = Column('standardized_state', String(140))
#    standardized_zip_code = Column('standardized_zip_code', String(140))
#    primary_phone_number = Column('primary_phone_number', String(140))
#    fax = Column('fax', String(140))
#    email = Column('email', String(140))
#    alternate_phone_numbers = Column('alternate_phone_numbers', String(140))
#    active_start_time = Column('active_start_time', DateTime)
#    active_end_time = Column('active_end_time', DateTime)
#    service_level = Column('service_level', String(140))
#    partner_account = Column('partner_account', String(140))
#    last_modified_at = Column('last_modified_at', DateTime)
#    cross_street = Column('cross_street', String(140))
#    record_change = Column('record_change', String(140))
#    old_service_level = Column('old_service_level', String(140))
#    version = Column('version', String(140))
#    npi = Column('npi', String(140))
#    directory_specialty_name = Column('directory_specialty_name', String(140))
#    replace_ncpdp = Column('replace_ncpdpd', String(140))
#    state_license_number = Column('state_license_number', String(140))
#    upin = Column('upin', String(140))
#    facility_id = Column('facility_id', String(140))
#    medicare_number = Column('medicare_number', String(140))
#    medicaid_number = Column('medicaid_number', String(140))
#    payer_id = Column('payer_id', String(140))
#    dea_number = Column('dea_number', String(140))
#    hin = Column('hin', String(140))
#    mutually_defined = Column('mutually_defined', String(140))
#    direct_address = Column('direct_address', String(140))
#    organization_type = Column('organization_type', String(140))
#    parent_organization_id = Column('parent_organization_id', Integer)
#    latitude = Column('latitude', Float(precision=None, asdecimal=False, decimal_return_scale=None))
#    longitude = Column('longitude', Float(precision=None, asdecimal=False, decimal_return_scale=None))
#    precise = Column('precise', String(140))
#    use_cases = Column('use_cases', String(140))
#    editable = Column('editable', Boolean)
#    
#    def __repr__(self):
#        return self.surescripts_organizations
#    
#class SurescriptsProviderLocations(AuditMixin, Integer):
#    __bind_key__ = 'app'
#    __tablename__ = 'surescripts_provider_locations'
#    
#    spi = Column('spi', Integer, primary_key=True)
#    npi = Column('npi', String(140))
#    dea_number = Column('dea_number', String(140))
#    state_license_number = Column('state_license_number', String(140))
#    speciality = Column('speciality', String(140))
#    prefix = Column('prefix', String(140))
#    last_name = Column('last_name', String(140))
#    first_name = Column('first_name', String(140))
#    middle_name = Column('first_name', String(140))
#    suffix = Column('suffix', String(140))
#    business_name = Column('business_name', String(140))
#    address_line_1 = Column('address_line_1', String(140))
#    address_line_2 = Column('address_line_2', String(140))
#    city = Column('city', String(140))
#    state = Column('state', String(140))
#    zip_code = Column('zip_code', String(140))
#    country_code = Column('country_code', String(140))
#    standardized_address_line_1 = Column('standardized_address_line_1', String(140))
#    standardized_address_line_2 = Column('standardized_address_line_2', String(140))
#    standardized_city = Column('standardized_city', String(140))
#    standardized_state = Column('standardized_state', String(140))
#    standardized_zip_code = Column('standardized_zip_code', String(140))
#    primary_phone_number = Column('primary_phone_number', String(140))
#    fax = Column('fax', String(140))
#    email = Column('email', String(140))
#    alternate_phone_numbers = Column('alternate_phone_numbers', String(140))
#    active_start_time = Column('active_start_time', DateTime)
#    active_end_time = Column('active_end_time', DateTime)
#    service_level = Column('service_level', String(140))
#    partner_account = Column('partner_account', String(140))
#    last_modified_at = Column('last_modified_at', DateTime)
#    record_change = Column('record_change', String(140))
#    old_service_level = Column('old_service_level', String(140))
#    version = Column('version', String(140))
#    directory_specialty_name = Column('directory_specialty_name', String(140))
#    medicare_number = Column('medicare_number', String(140))
#    medicaid_number = Column('medicaid_number', String(140))
#    upin = Column('upin', String(140))
#    certificate_to_prescribe = Column('certificate_to_prescribe', String(140))
#    data_2000_waiver_id = Column('data_2000_waiver_id', String(140))
#    rems_healthcare_provider_enrollment_id = Column('rems_healthcare_provider_enrollment_id', String(140))
#    state_controlled_substance_number = Column('state_controlled_substance_number', String(140))
#    mutually_defined = Column('mutually_defined', String(140))
#    direct_address = Column('direct_address', String(140))
#    use_cases = Column('use_cases', String(140))
#    available_routes = Column('available_routes', String(140))
#    organization_id = Column('organization_id', Integer)
#    latitude = Column('latitude', Float(precision=None, asdecimal=False, decimal_return_scale=None))
#    longitude = Column('longitude', Float(precision=None, asdecimal=False, decimal_return_scale=None))
#    precise = Column('precise', String(140))
#    editable = Column('editable', Boolean) 
#
#    def __repr__(self):
#        return self.surescripts_provider_locations
#        
#class SurescriptsRequests(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'surescripts_requests'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    body = Column('body', String(140))
#    message_type = Column('message_type', String(140))
#    
#    def __repr__(self):
#        return self.surescripts_requests
#        
#class SurveyResponses(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'survey_responses'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #company_user_id = Column('company_user_id', Integer)
#    lab_test_group_name = Column('lab_test_group_name', String(140))
#    answers = Column('answers', JSON)
#    
#    company_user_id = Column('company_user_id', Integer, ForeignKey("company_users.id"), nullable=False)
#    company_users = relationship("CompanyUsers")
#
#    def __repr__(self):
#        return self.survey_responses
        
#class Transfers(AuditMixin, Model):
#    __bind_key__ = 'app'
#    __tablename__ = 'transfers'
#    
#    id = Column('id', Integer, primary_key=True, autoincrement=True)
#    #prescription_id = Column('prescription_id', Integer)
#    state = Column('state', String(140))
#    
#    prescription_id = Column('prescription_id', Integer, ForeignKey("prescriptions.id"), nullable=False)
#    prescriptions = relationship("Prescriptions")
#
#    def __repr__(self):
#        return self.transfers


        
        

        

 
db.create_all()
