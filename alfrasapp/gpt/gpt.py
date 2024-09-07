import frappe
import frappe.desk.search
from frappe import whitelist
from frappe.desk.search import search_link
import json
import os
import json
import openai
import re



# قائمة لتخزين سجل المحادثات
conversation_history_SerchALL = [
    {"role": "system", "content": "Consider yourself an expert at identifying erpnext link paths starting with '/app/' when I say open interface or similar..",
    },{"role": "assistant", "content": '''     {
        "Type": "doctype",
        "english_name": "KSA VAT Setting",
        "arabic_name": "KSA VAT Setting",
        "link": "/app/ksa-vat-setting"
    },
    {
        "Type": "doctype",
        "english_name": "Print Heading",
        "arabic_name": "Print Heading",
        "link": "/app/print-heading"
    },
    {
        "Type": "doctype",
        "english_name": "Tax Settings",
        "arabic_name": "Tax Settings",
        "link": "/app/tax-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Warehouse",
        "arabic_name": "Warehouse",
        "link": "/app/warehouse"
    },
    {
        "Type": "doctype",
        "english_name": "Process Statement Of Accounts",
        "arabic_name": "Process Statement Of Accounts",
        "link": "/app/process-statement-of-accounts"
    },
    {
        "Type": "doctype",
        "english_name": "Web Form",
        "arabic_name": "Web Form",
        "link": "/app/web-form"
    },
    {
        "Type": "doctype",
        "english_name": "Purchase Invoice",
        "arabic_name": "Purchase Invoice",
        "link": "/app/purchase-invoice"
    },
    {
        "Type": "doctype",
        "english_name": "Company",
        "arabic_name": "Company",
        "link": "/app/company"
    },
    {
        "Type": "doctype",
        "english_name": "Journal Entry",
        "arabic_name": "Journal Entry",
        "link": "/app/journal-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Invoice",
        "arabic_name": "Sales Invoice",
        "link": "/app/sales-invoice"
    },
    {
        "Type": "doctype",
        "english_name": "Notification",
        "arabic_name": "Notification",
        "link": "/app/notification"
    },
    {
        "Type": "doctype",
        "english_name": "Department",
        "arabic_name": "Department",
        "link": "/app/department"
    },
    {
        "Type": "doctype",
        "english_name": "Repost Accounting Ledger Settings",
        "arabic_name": "Repost Accounting Ledger Settings",
        "link": "/app/repost-accounting-ledger-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Repost Payment Ledger",
        "arabic_name": "Repost Payment Ledger",
        "link": "/app/repost-payment-ledger"
    },
    {
        "Type": "doctype",
        "english_name": "Repost Accounting Ledger",
        "arabic_name": "Repost Accounting Ledger",
        "link": "/app/repost-accounting-ledger"
    },
    {
        "Type": "doctype",
        "english_name": "Dashboard Chart",
        "arabic_name": "Dashboard Chart",
        "link": "/app/dashboard-chart"
    },
    {
        "Type": "doctype",
        "english_name": "Fiscal Year",
        "arabic_name": "Fiscal Year",
        "link": "/app/fiscal-year"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Order",
        "arabic_name": "Sales Order",
        "link": "/app/sales-order"
    },
    {
        "Type": "doctype",
        "english_name": "Pricing Rule",
        "arabic_name": "Pricing Rule",
        "link": "/app/pricing-rule"
    },
    {
        "Type": "doctype",
        "english_name": "File",
        "arabic_name": "File",
        "link": "/app/file"
    },
    {
        "Type": "doctype",
        "english_name": "Customer",
        "arabic_name": "Customer",
        "link": "/app/customer"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier",
        "arabic_name": "Supplier",
        "link": "/app/supplier"
    },
    {
        "Type": "doctype",
        "english_name": "System Health Report",
        "arabic_name": "System Health Report",
        "link": "/app/system-health-report"
    },
    {
        "Type": "doctype",
        "english_name": "Data Import Log",
        "arabic_name": "Data Import Log",
        "link": "/app/data-import-log"
    },
    {
        "Type": "doctype",
        "english_name": "OAuth Client",
        "arabic_name": "OAuth Client",
        "link": "/app/oauth-client"
    },
    {
        "Type": "doctype",
        "english_name": "Stock Reposting Settings",
        "arabic_name": "Stock Reposting Settings",
        "link": "/app/stock-reposting-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Project",
        "arabic_name": "Project",
        "link": "/app/project"
    },
    {
        "Type": "doctype",
        "english_name": "Cost Center",
        "arabic_name": "Cost Center",
        "link": "/app/cost-center"
    },
    {
        "Type": "doctype",
        "english_name": "Lower Deduction Certificate",
        "arabic_name": "Lower Deduction Certificate",
        "link": "/app/lower-deduction-certificate"
    },
    {
        "Type": "doctype",
        "english_name": "Web Page",
        "arabic_name": "Web Page",
        "link": "/app/web-page"
    },
    {
        "Type": "doctype",
        "english_name": "Letter Head",
        "arabic_name": "Letter Head",
        "link": "/app/letter-head"
    },
    {
        "Type": "doctype",
        "english_name": "Ledger Health",
        "arabic_name": "Ledger Health",
        "link": "/app/ledger-health"
    },
    {
        "Type": "doctype",
        "english_name": "Changelog Feed",
        "arabic_name": "Changelog Feed",
        "link": "/app/changelog-feed"
    },
    {
        "Type": "doctype",
        "english_name": "Server Script",
        "arabic_name": "Server Script",
        "link": "/app/server-script"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Quotation",
        "arabic_name": "Supplier Quotation",
        "link": "/app/supplier-quotation"
    },
    {
        "Type": "doctype",
        "english_name": "Pick List",
        "arabic_name": "Pick List",
        "link": "/app/pick-list"
    },
    {
        "Type": "doctype",
        "english_name": "Communication",
        "arabic_name": "Communication",
        "link": "/app/communication"
    },
    {
        "Type": "doctype",
        "english_name": "Ledger Health Monitor",
        "arabic_name": "Ledger Health Monitor",
        "link": "/app/ledger-health-monitor"
    },
    {
        "Type": "doctype",
        "english_name": "System Settings",
        "arabic_name": "System Settings",
        "link": "/app/system-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Transaction Deletion Record",
        "arabic_name": "Transaction Deletion Record",
        "link": "/app/transaction-deletion-record"
    },
    {
        "Type": "doctype",
        "english_name": "Purchase Receipt",
        "arabic_name": "Purchase Receipt",
        "link": "/app/purchase-receipt"
    },
    {
        "Type": "doctype",
        "english_name": "Delivery Note",
        "arabic_name": "Delivery Note",
        "link": "/app/delivery-note"
    },
    {
        "Type": "doctype",
        "english_name": "Quotation",
        "arabic_name": "Quotation",
        "link": "/app/quotation"
    },
    {
        "Type": "doctype",
        "english_name": "Purchase Order",
        "arabic_name": "Purchase Order",
        "link": "/app/purchase-order"
    },
    {
        "Type": "doctype",
        "english_name": "POS Invoice",
        "arabic_name": "POS Invoice",
        "link": "/app/pos-invoice"
    },
    {
        "Type": "doctype",
        "english_name": "GL Entry",
        "arabic_name": "GL Entry",
        "link": "/app/gl-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Currency Exchange Settings",
        "arabic_name": "Currency Exchange Settings",
        "link": "/app/currency-exchange-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Role",
        "arabic_name": "Role",
        "link": "/app/role"
    },
    {
        "Type": "doctype",
        "english_name": "Item Price",
        "arabic_name": "Item Price",
        "link": "/app/item-price"
    },
    {
        "Type": "doctype",
        "english_name": "Console Log",
        "arabic_name": "Console Log",
        "link": "/app/console-log"
    },
    {
        "Type": "doctype",
        "english_name": "Custom Field",
        "arabic_name": "Custom Field",
        "link": "/app/custom-field"
    },
    {
        "Type": "doctype",
        "english_name": "RQ Worker",
        "arabic_name": "RQ Worker",
        "link": "/app/rq-worker"
    },
    {
        "Type": "doctype",
        "english_name": "Production Plan",
        "arabic_name": "Production Plan",
        "link": "/app/production-plan"
    },
    {
        "Type": "doctype",
        "english_name": "Item Group",
        "arabic_name": "Item Group",
        "link": "/app/item-group"
    },
    {
        "Type": "doctype",
        "english_name": "Work Order",
        "arabic_name": "Work Order",
        "link": "/app/work-order"
    },
    {
        "Type": "doctype",
        "english_name": "User",
        "arabic_name": "User",
        "link": "/app/user"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Stock Ledger Entry",
        "arabic_name": "Stock Ledger Entry",
        "link": "/app/stock-ledger-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Webhook",
        "arabic_name": "Webhook",
        "link": "/app/webhook"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Account",
        "arabic_name": "Bank Account",
        "link": "/app/bank-account"
    },
    {
        "Type": "doctype",
        "english_name": "Data Import",
        "arabic_name": "Data Import",
        "link": "/app/data-import"
    },
    {
        "Type": "doctype",
        "english_name": "Google Settings",
        "arabic_name": "Google Settings",
        "link": "/app/google-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Asset",
        "arabic_name": "Asset",
        "link": "/app/asset"
    },
    {
        "Type": "doctype",
        "english_name": "RQ Job",
        "arabic_name": "RQ Job",
        "link": "/app/rq-job"
    },
    {
        "Type": "doctype",
        "english_name": "Buying Settings",
        "arabic_name": "Buying Settings",
        "link": "/app/buying-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Stock Entry",
        "arabic_name": "Stock Entry",
        "link": "/app/stock-entry"
    },
    {
        "Type": "doctype",
        "english_name": "E Commerce Settings",
        "arabic_name": "E Commerce Settings",
        "link": "/app/e-commerce-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Item",
        "arabic_name": "Item",
        "link": "/app/item"
    },
    {
        "Type": "doctype",
        "english_name": "Employee",
        "arabic_name": "Employee",
        "link": "/app/employee"
    },
    {
        "Type": "doctype",
        "english_name": "Help Article",
        "arabic_name": "Help Article",
        "link": "/app/help-article"
    },
    {
        "Type": "doctype",
        "english_name": "Manufacturing Settings",
        "arabic_name": "Manufacturing Settings",
        "link": "/app/manufacturing-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Cashier Closing",
        "arabic_name": "Cashier Closing",
        "link": "/app/cashier-closing"
    },
    {
        "Type": "doctype",
        "english_name": "BOM",
        "arabic_name": "BOM",
        "link": "/app/bom"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Reconciliation",
        "arabic_name": "Payment Reconciliation",
        "link": "/app/payment-reconciliation"
    },
    {
        "Type": "doctype",
        "english_name": "Web Template",
        "arabic_name": "Web Template",
        "link": "/app/web-template"
    },
    {
        "Type": "doctype",
        "english_name": "Email Template",
        "arabic_name": "Email Template",
        "link": "/app/email-template"
    },
    {
        "Type": "doctype",
        "english_name": "Print Format",
        "arabic_name": "Print Format",
        "link": "/app/print-format"
    },
    {
        "Type": "doctype",
        "english_name": "Route History",
        "arabic_name": "Route History",
        "link": "/app/route-history"
    },
    {
        "Type": "doctype",
        "english_name": "Lead",
        "arabic_name": "Lead",
        "link": "/app/lead"
    },
    {
        "Type": "doctype",
        "english_name": "DocType",
        "arabic_name": "DocType",
        "link": "/app/doctype"
    },
    {
        "Type": "doctype",
        "english_name": "Customize Form",
        "arabic_name": "Customize Form",
        "link": "/app/customize-form"
    },
    {
        "Type": "doctype",
        "english_name": "Bisect Nodes",
        "arabic_name": "Bisect Nodes",
        "link": "/app/bisect-nodes"
    },
    {
        "Type": "doctype",
        "english_name": "Bisect Accounting Statements",
        "arabic_name": "Bisect Accounting Statements",
        "link": "/app/bisect-accounting-statements"
    },
    {
        "Type": "doctype",
        "english_name": "Notification Settings",
        "arabic_name": "Notification Settings",
        "link": "/app/notification-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Shift Factor",
        "arabic_name": "Asset Shift Factor",
        "link": "/app/asset-shift-factor"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Shift Allocation",
        "arabic_name": "Asset Shift Allocation",
        "link": "/app/asset-shift-allocation"
    },
    {
        "Type": "doctype",
        "english_name": "Warranty Claim",
        "arabic_name": "Warranty Claim",
        "link": "/app/warranty-claim"
    },
    {
        "Type": "doctype",
        "english_name": "Email Group",
        "arabic_name": "Email Group",
        "link": "/app/email-group"
    },
    {
        "Type": "doctype",
        "english_name": "Competitor",
        "arabic_name": "Competitor",
        "link": "/app/competitor"
    },
    {
        "Type": "doctype",
        "english_name": "Quotation Lost Reason",
        "arabic_name": "Quotation Lost Reason",
        "link": "/app/quotation-lost-reason"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Entry",
        "arabic_name": "Payment Entry",
        "link": "/app/payment-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Product Bundle",
        "arabic_name": "Product Bundle",
        "link": "/app/product-bundle"
    },
    {
        "Type": "doctype",
        "english_name": "Address",
        "arabic_name": "Address",
        "link": "/app/address"
    },
    {
        "Type": "doctype",
        "english_name": "Accounts Settings",
        "arabic_name": "Accounts Settings",
        "link": "/app/accounts-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Subcontracting Receipt",
        "arabic_name": "Subcontracting Receipt",
        "link": "/app/subcontracting-receipt"
    },
    {
        "Type": "doctype",
        "english_name": "Bulk Transaction Log",
        "arabic_name": "Bulk Transaction Log",
        "link": "/app/bulk-transaction-log"
    },
    {
        "Type": "doctype",
        "english_name": "Bulk Transaction Log Detail",
        "arabic_name": "Bulk Transaction Log Detail",
        "link": "/app/bulk-transaction-log-detail"
    },
    {
        "Type": "doctype",
        "english_name": "Number Card",
        "arabic_name": "Number Card",
        "link": "/app/number-card"
    },
    {
        "Type": "doctype",
        "english_name": "Batch",
        "arabic_name": "Batch",
        "link": "/app/batch"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Ledger Entry",
        "arabic_name": "Payment Ledger Entry",
        "link": "/app/payment-ledger-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Request for Quotation",
        "arabic_name": "Request for Quotation",
        "link": "/app/request-for-quotation"
    },
    {
        "Type": "doctype",
        "english_name": "Process Payment Reconciliation Log",
        "arabic_name": "Process Payment Reconciliation Log",
        "link": "/app/process-payment-reconciliation-log"
    },
    {
        "Type": "doctype",
        "english_name": "Bin",
        "arabic_name": "Bin",
        "link": "/app/bin"
    },
    {
        "Type": "doctype",
        "english_name": "Audit Trail",
        "arabic_name": "Audit Trail",
        "link": "/app/audit-trail"
    },
    {
        "Type": "doctype",
        "english_name": "Selling Settings",
        "arabic_name": "Selling Settings",
        "link": "/app/selling-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Integration Request",
        "arabic_name": "Integration Request",
        "link": "/app/integration-request"
    },
    {
        "Type": "doctype",
        "english_name": "Contact",
        "arabic_name": "Contact",
        "link": "/app/contact"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Inventory Dimension",
        "arabic_name": "Inventory Dimension",
        "link": "/app/inventory-dimension"
    },
    {
        "Type": "doctype",
        "english_name": "ToDo",
        "arabic_name": "ToDo",
        "link": "/app/todo"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Capitalization",
        "arabic_name": "Asset Capitalization",
        "link": "/app/asset-capitalization"
    },
    {
        "Type": "doctype",
        "english_name": "Task",
        "arabic_name": "Task",
        "link": "/app/task"
    },
    {
        "Type": "doctype",
        "english_name": "Material Request",
        "arabic_name": "Material Request",
        "link": "/app/material-request"
    },
    {
        "Type": "doctype",
        "english_name": "Website Item",
        "arabic_name": "Website Item",
        "link": "/app/website-item"
    },
    {
        "Type": "doctype",
        "english_name": "Period Closing Voucher",
        "arabic_name": "Period Closing Voucher",
        "link": "/app/period-closing-voucher"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Repayment",
        "arabic_name": "Loan Repayment",
        "link": "/app/loan-repayment"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Procedure",
        "arabic_name": "Quality Procedure",
        "link": "/app/quality-procedure"
    },
    {
        "Type": "doctype",
        "english_name": "Location",
        "arabic_name": "Location",
        "link": "/app/location"
    },
    {
        "Type": "doctype",
        "english_name": "Unreconcile Payment",
        "arabic_name": "Unreconcile Payment",
        "link": "/app/unreconcile-payment"
    },
    {
        "Type": "doctype",
        "english_name": "Process Payment Reconciliation",
        "arabic_name": "Process Payment Reconciliation",
        "link": "/app/process-payment-reconciliation"
    },
    {
        "Type": "doctype",
        "english_name": "Non Conformance",
        "arabic_name": "Non Conformance",
        "link": "/app/non-conformance"
    },
    {
        "Type": "doctype",
        "english_name": "Activity Log",
        "arabic_name": "Activity Log",
        "link": "/app/activity-log"
    },
    {
        "Type": "doctype",
        "english_name": "Comment",
        "arabic_name": "Comment",
        "link": "/app/comment"
    },
    {
        "Type": "doctype",
        "english_name": "Holiday List",
        "arabic_name": "Holiday List",
        "link": "/app/holiday-list"
    },
    {
        "Type": "doctype",
        "english_name": "Global Defaults",
        "arabic_name": "Global Defaults",
        "link": "/app/global-defaults"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Movement",
        "arabic_name": "Asset Movement",
        "link": "/app/asset-movement"
    },
    {
        "Type": "doctype",
        "english_name": "Delivery Trip",
        "arabic_name": "Delivery Trip",
        "link": "/app/delivery-trip"
    },
    {
        "Type": "doctype",
        "english_name": "DoppioBot Settings",
        "arabic_name": "DoppioBot Settings",
        "link": "/app/doppiobot-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Exchange Rate Revaluation",
        "arabic_name": "Exchange Rate Revaluation",
        "link": "/app/exchange-rate-revaluation"
    },
    {
        "Type": "doctype",
        "english_name": "DocShare",
        "arabic_name": "DocShare",
        "link": "/app/docshare"
    },
    {
        "Type": "doctype",
        "english_name": "Notification Log",
        "arabic_name": "Notification Log",
        "link": "/app/notification-log"
    },
    {
        "Type": "doctype",
        "english_name": "Job Card",
        "arabic_name": "Job Card",
        "link": "/app/job-card"
    },
    {
        "Type": "doctype",
        "english_name": "Email Queue",
        "arabic_name": "Email Queue",
        "link": "/app/email-queue"
    },
    {
        "Type": "doctype",
        "english_name": "Workspace",
        "arabic_name": "Workspace",
        "link": "/app/workspace"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Transaction",
        "arabic_name": "Bank Transaction",
        "link": "/app/bank-transaction"
    },
    {
        "Type": "doctype",
        "english_name": "Email Account",
        "arabic_name": "Email Account",
        "link": "/app/email-account"
    },
    {
        "Type": "doctype",
        "english_name": "Email Domain",
        "arabic_name": "Email Domain",
        "link": "/app/email-domain"
    },
    {
        "Type": "doctype",
        "english_name": "Stock Settings",
        "arabic_name": "Stock Settings",
        "link": "/app/stock-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Custom HTML Block",
        "arabic_name": "Custom HTML Block",
        "link": "/app/custom-html-block"
    },
    {
        "Type": "doctype",
        "english_name": "Form Tour",
        "arabic_name": "Form Tour",
        "link": "/app/form-tour"
    },
    {
        "Type": "doctype",
        "english_name": "Closing Stock Balance",
        "arabic_name": "Closing Stock Balance",
        "link": "/app/closing-stock-balance"
    },
    {
        "Type": "doctype",
        "english_name": "Patch Log",
        "arabic_name": "Patch Log",
        "link": "/app/patch-log"
    },
    {
        "Type": "doctype",
        "english_name": "Packing Slip",
        "arabic_name": "Packing Slip",
        "link": "/app/packing-slip"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''{
        "Type": "doctype",
        "english_name": "Document Naming Rule",
        "arabic_name": "Document Naming Rule",
        "link": "/app/document-naming-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Service Level Agreement",
        "arabic_name": "Service Level Agreement",
        "link": "/app/service-level-agreement"
    },
    {
        "Type": "doctype",
        "english_name": "Timesheet",
        "arabic_name": "Timesheet",
        "link": "/app/timesheet"
    },
    {
        "Type": "doctype",
        "english_name": "Serial No",
        "arabic_name": "Serial No",
        "link": "/app/serial-no"
    },
    {
        "Type": "doctype",
        "english_name": "Workflow Action Master",
        "arabic_name": "Workflow Action Master",
        "link": "/app/workflow-action-master"
    },
    {
        "Type": "doctype",
        "english_name": "Language",
        "arabic_name": "Language",
        "link": "/app/language"
    },
    {
        "Type": "doctype",
        "english_name": "Account",
        "arabic_name": "Account",
        "link": "/app/account"
    },
    {
        "Type": "doctype",
        "english_name": "Shareholder",
        "arabic_name": "Shareholder",
        "link": "/app/shareholder"
    },
    {
        "Type": "doctype",
        "english_name": "Report",
        "arabic_name": "Report",
        "link": "/app/report"
    },
    {
        "Type": "doctype",
        "english_name": "OAuth Bearer Token",
        "arabic_name": "OAuth Bearer Token",
        "link": "/app/oauth-bearer-token"
    },
    {
        "Type": "doctype",
        "english_name": "Workflow State",
        "arabic_name": "Workflow State",
        "link": "/app/workflow-state"
    },
    {
        "Type": "doctype",
        "english_name": "Dropbox Settings",
        "arabic_name": "Dropbox Settings",
        "link": "/app/dropbox-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Reconciliation Tool",
        "arabic_name": "Bank Reconciliation Tool",
        "link": "/app/bank-reconciliation-tool"
    },
    {
        "Type": "doctype",
        "english_name": "Account Closing Balance",
        "arabic_name": "Account Closing Balance",
        "link": "/app/account-closing-balance"
    },
    {
        "Type": "doctype",
        "english_name": "Webhook Request Log",
        "arabic_name": "Webhook Request Log",
        "link": "/app/webhook-request-log"
    },
    {
        "Type": "doctype",
        "english_name": "Blog Post",
        "arabic_name": "Blog Post",
        "link": "/app/blog-post"
    },
    {
        "Type": "doctype",
        "english_name": "DocType Layout",
        "arabic_name": "DocType Layout",
        "link": "/app/doctype-layout"
    },
    {
        "Type": "doctype",
        "english_name": "Industry Type",
        "arabic_name": "Industry Type",
        "link": "/app/industry-type"
    },
    {
        "Type": "doctype",
        "english_name": "Designation",
        "arabic_name": "Designation",
        "link": "/app/designation"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Stage",
        "arabic_name": "Sales Stage",
        "link": "/app/sales-stage"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Partner Type",
        "arabic_name": "Sales Partner Type",
        "link": "/app/sales-partner-type"
    },
    {
        "Type": "doctype",
        "english_name": "Lead Source",
        "arabic_name": "Lead Source",
        "link": "/app/lead-source"
    },
    {
        "Type": "doctype",
        "english_name": "Terms and Conditions",
        "arabic_name": "Terms and Conditions",
        "link": "/app/terms-and-conditions"
    },
    {
        "Type": "doctype",
        "english_name": "LDAP Settings",
        "arabic_name": "LDAP Settings",
        "link": "/app/ldap-settings"
    },
    {
        "Type": "doctype",
        "english_name": "S3 Backup Settings",
        "arabic_name": "S3 Backup Settings",
        "link": "/app/s3-backup-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Token Cache",
        "arabic_name": "Token Cache",
        "link": "/app/token-cache"
    },
    {
        "Type": "doctype",
        "english_name": "Territory",
        "arabic_name": "Territory",
        "link": "/app/territory"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Group",
        "arabic_name": "Supplier Group",
        "link": "/app/supplier-group"
    },
    {
        "Type": "doctype",
        "english_name": "Customer Group",
        "arabic_name": "Customer Group",
        "link": "/app/customer-group"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Request",
        "arabic_name": "Payment Request",
        "link": "/app/payment-request"
    },
    {
        "Type": "doctype",
        "english_name": "Appointment",
        "arabic_name": "Appointment",
        "link": "/app/appointment"
    },
    {
        "Type": "doctype",
        "english_name": "Appointment Booking Settings",
        "arabic_name": "Appointment Booking Settings",
        "link": "/app/appointment-booking-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Website Settings",
        "arabic_name": "Website Settings",
        "link": "/app/website-settings"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Google Drive",
        "arabic_name": "Google Drive",
        "link": "/app/google-drive"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Clearance",
        "arabic_name": "Bank Clearance",
        "link": "/app/bank-clearance"
    },
    {
        "Type": "doctype",
        "english_name": "Repost Item Valuation",
        "arabic_name": "Repost Item Valuation",
        "link": "/app/repost-item-valuation"
    },
    {
        "Type": "doctype",
        "english_name": "Incoterm",
        "arabic_name": "Incoterm",
        "link": "/app/incoterm"
    },
    {
        "Type": "doctype",
        "english_name": "Shipment",
        "arabic_name": "Shipment",
        "link": "/app/shipment"
    },
    {
        "Type": "doctype",
        "english_name": "Workstation Type",
        "arabic_name": "Workstation Type",
        "link": "/app/workstation-type"
    },
    {
        "Type": "doctype",
        "english_name": "Workstation",
        "arabic_name": "Workstation",
        "link": "/app/workstation"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Type",
        "arabic_name": "Loan Type",
        "link": "/app/loan-type"
    },
    {
        "Type": "doctype",
        "english_name": "Opportunity",
        "arabic_name": "Opportunity",
        "link": "/app/opportunity"
    },
    {
        "Type": "doctype",
        "english_name": "Prospect",
        "arabic_name": "Prospect",
        "link": "/app/prospect"
    },
    {
        "Type": "doctype",
        "english_name": "Budget",
        "arabic_name": "Budget",
        "link": "/app/budget"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Inspection",
        "arabic_name": "Quality Inspection",
        "link": "/app/quality-inspection"
    },
    {
        "Type": "doctype",
        "english_name": "Loan",
        "arabic_name": "Loan",
        "link": "/app/loan"
    },
    {
        "Type": "doctype",
        "english_name": "Energy Point Log",
        "arabic_name": "Energy Point Log",
        "link": "/app/energy-point-log"
    },
    {
        "Type": "doctype",
        "english_name": "Web Page View",
        "arabic_name": "Web Page View",
        "link": "/app/web-page-view"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Statement Import",
        "arabic_name": "Bank Statement Import",
        "link": "/app/bank-statement-import"
    },
    {
        "Type": "doctype",
        "english_name": "Task Type",
        "arabic_name": "Task Type",
        "link": "/app/task-type"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Repair",
        "arabic_name": "Asset Repair",
        "link": "/app/asset-repair"
    },
    {
        "Type": "doctype",
        "english_name": "Subcontracting Order",
        "arabic_name": "Subcontracting Order",
        "link": "/app/subcontracting-order"
    },
    {
        "Type": "doctype",
        "english_name": "Event",
        "arabic_name": "Event",
        "link": "/app/event"
    },
    {
        "Type": "doctype",
        "english_name": "POS Profile",
        "arabic_name": "POS Profile",
        "link": "/app/pos-profile"
    },
    {
        "Type": "doctype",
        "english_name": "Salutation",
        "arabic_name": "Salutation",
        "link": "/app/salutation"
    },
    {
        "Type": "doctype",
        "english_name": "Gender",
        "arabic_name": "Gender",
        "link": "/app/gender"
    },
    {
        "Type": "doctype",
        "english_name": "Country",
        "arabic_name": "Country",
        "link": "/app/country"
    },
    {
        "Type": "doctype",
        "english_name": "POS Closing Entry",
        "arabic_name": "POS Closing Entry",
        "link": "/app/pos-closing-entry"
    },
    {
        "Type": "doctype",
        "english_name": "POS Invoice Merge Log",
        "arabic_name": "POS Invoice Merge Log",
        "link": "/app/pos-invoice-merge-log"
    },
    {
        "Type": "doctype",
        "english_name": "Blog Settings",
        "arabic_name": "Blog Settings",
        "link": "/app/blog-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Email Group Member",
        "arabic_name": "Email Group Member",
        "link": "/app/email-group-member"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Balance Adjustment",
        "arabic_name": "Loan Balance Adjustment",
        "link": "/app/loan-balance-adjustment"
    },
    {
        "Type": "doctype",
        "english_name": "Currency",
        "arabic_name": "Currency",
        "link": "/app/currency"
    },
    {
        "Type": "doctype",
        "english_name": "Translation",
        "arabic_name": "Translation",
        "link": "/app/translation"
    },
    {
        "Type": "doctype",
        "english_name": "Authorization Rule",
        "arabic_name": "Authorization Rule",
        "link": "/app/authorization-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Security Shortfall",
        "arabic_name": "Loan Security Shortfall",
        "link": "/app/loan-security-shortfall"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Interest Accrual",
        "arabic_name": "Loan Interest Accrual",
        "link": "/app/loan-interest-accrual"
    },
    {
        "Type": "doctype",
        "english_name": "Process Loan Interest Accrual",
        "arabic_name": "Process Loan Interest Accrual",
        "link": "/app/process-loan-interest-accrual"
    },
    {
        "Type": "doctype",
        "english_name": "Driver",
        "arabic_name": "Driver",
        "link": "/app/driver"
    },
    {
        "Type": "doctype",
        "english_name": "Scheduled Job Type",
        "arabic_name": "Scheduled Job Type",
        "link": "/app/scheduled-job-type"
    },
    {
        "Type": "doctype",
        "english_name": "Vehicle",
        "arabic_name": "Vehicle",
        "link": "/app/vehicle"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Refund",
        "arabic_name": "Loan Refund",
        "link": "/app/loan-refund"
    },
    {
        "Type": "doctype",
        "english_name": "BOM Update Log",
        "arabic_name": "BOM Update Log",
        "link": "/app/bom-update-log"
    },
    {
        "Type": "doctype",
        "english_name": "Error Log",
        "arabic_name": "Error Log",
        "link": "/app/error-log"
    },
    {
        "Type": "doctype",
        "english_name": "Access Log",
        "arabic_name": "Access Log",
        "link": "/app/access-log"
    },
    {
        "Type": "doctype",
        "english_name": "Deleted Document",
        "arabic_name": "Deleted Document",
        "link": "/app/deleted-document"
    },
    {
        "Type": "doctype",
        "english_name": "Scheduled Job Log",
        "arabic_name": "Scheduled Job Log",
        "link": "/app/scheduled-job-log"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Log Settings",
        "arabic_name": "Log Settings",
        "link": "/app/log-settings"
    },
    {
        "Type": "doctype",
        "english_name": "User Type",
        "arabic_name": "User Type",
        "link": "/app/user-type"
    },
    {
        "Type": "doctype",
        "english_name": "CRM Settings",
        "arabic_name": "CRM Settings",
        "link": "/app/crm-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Document Naming Settings",
        "arabic_name": "Document Naming Settings",
        "link": "/app/document-naming-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Purchase Taxes and Charges Template",
        "arabic_name": "Purchase Taxes and Charges Template",
        "link": "/app/purchase-taxes-and-charges-template"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Taxes and Charges Template",
        "arabic_name": "Sales Taxes and Charges Template",
        "link": "/app/sales-taxes-and-charges-template"
    },
    {
        "Type": "doctype",
        "english_name": "Stock Reconciliation",
        "arabic_name": "Stock Reconciliation",
        "link": "/app/stock-reconciliation"
    },
    {
        "Type": "doctype",
        "english_name": "Prepared Report",
        "arabic_name": "Prepared Report",
        "link": "/app/prepared-report"
    },
    {
        "Type": "doctype",
        "english_name": "System Console",
        "arabic_name": "System Console",
        "link": "/app/system-console"
    },
    {
        "Type": "doctype",
        "english_name": "Call Log",
        "arabic_name": "Call Log",
        "link": "/app/call-log"
    },
    {
        "Type": "doctype",
        "english_name": "Kanban Board",
        "arabic_name": "Kanban Board",
        "link": "/app/kanban-board"
    },
    {
        "Type": "doctype",
        "english_name": "Client Script",
        "arabic_name": "Client Script",
        "link": "/app/client-script"
    },
    {
        "Type": "doctype",
        "english_name": "Newsletter",
        "arabic_name": "Newsletter",
        "link": "/app/newsletter"
    },
    {
        "Type": "doctype",
        "english_name": "Property Setter",
        "arabic_name": "Property Setter",
        "link": "/app/property-setter"
    },
    {
        "Type": "doctype",
        "english_name": "Telephony Call Type",
        "arabic_name": "Telephony Call Type",
        "link": "/app/telephony-call-type"
    },
    {
        "Type": "doctype",
        "english_name": "Workflow Action",
        "arabic_name": "Workflow Action",
        "link": "/app/workflow-action"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Disbursement",
        "arabic_name": "Loan Disbursement",
        "link": "/app/loan-disbursement"
    },
    {
        "Type": "doctype",
        "english_name": "Opportunity Lost Reason",
        "arabic_name": "Opportunity Lost Reason",
        "link": "/app/opportunity-lost-reason"
    },
    {
        "Type": "doctype",
        "english_name": "GoCardless Settings",
        "arabic_name": "GoCardless Settings",
        "link": "/app/gocardless-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Cost Center Allocation",
        "arabic_name": "Cost Center Allocation",
        "link": "/app/cost-center-allocation"
    },
    {
        "Type": "doctype",
        "english_name": "Tax Category",
        "arabic_name": "Tax Category",
        "link": "/app/tax-category"
    },
    {
        "Type": "doctype",
        "english_name": "Item Tax Template",
        "arabic_name": "Item Tax Template",
        "link": "/app/item-tax-template"
    },
    {
        "Type": "doctype",
        "english_name": "Document Share Key",
        "arabic_name": "Document Share Key",
        "link": "/app/document-share-key"
    },
    {
        "Type": "doctype",
        "english_name": "Connected App",
        "arabic_name": "Connected App",
        "link": "/app/connected-app"
    },
    {
        "Type": "doctype",
        "english_name": "Opening Invoice Creation Tool",
        "arabic_name": "Opening Invoice Creation Tool",
        "link": "/app/opening-invoice-creation-tool"
    },
    {
        "Type": "doctype",
        "english_name": "Module Def",
        "arabic_name": "Module Def",
        "link": "/app/module-def"
    },
    {
        "Type": "doctype",
        "english_name": "User Permission",
        "arabic_name": "User Permission",
        "link": "/app/user-permission"
    },
    {
        "Type": "doctype",
        "english_name": "Maintenance Visit",
        "arabic_name": "Maintenance Visit",
        "link": "/app/maintenance-visit"
    },
    {
        "Type": "doctype",
        "english_name": "Personal Data Deletion Request",
        "arabic_name": "Personal Data Deletion Request",
        "link": "/app/personal-data-deletion-request"
    },
    {
        "Type": "doctype",
        "english_name": "Ledger Merge",
        "arabic_name": "Ledger Merge",
        "link": "/app/ledger-merge"
    },
    {
        "Type": "doctype",
        "english_name": "Subscription Plan",
        "arabic_name": "Subscription Plan",
        "link": "/app/subscription-plan"
    },
    {
        "Type": "doctype",
        "english_name": "Module Profile",
        "arabic_name": "Module Profile",
        "link": "/app/module-profile"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": ''' {
        "Type": "doctype",
        "english_name": "Role Profile",
        "arabic_name": "Role Profile",
        "link": "/app/role-profile"
    },
    {
        "Type": "doctype",
        "english_name": "Onboarding Step",
        "arabic_name": "Onboarding Step",
        "link": "/app/onboarding-step"
    },
    {
        "Type": "doctype",
        "english_name": "TaxJar Settings",
        "arabic_name": "TaxJar Settings",
        "link": "/app/taxjar-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Email Flag Queue",
        "arabic_name": "Email Flag Queue",
        "link": "/app/email-flag-queue"
    },
    {
        "Type": "doctype",
        "english_name": "Operation",
        "arabic_name": "Operation",
        "link": "/app/operation"
    },
    {
        "Type": "doctype",
        "english_name": "Issue",
        "arabic_name": "Issue",
        "link": "/app/issue"
    },
    {
        "Type": "doctype",
        "english_name": "Energy Point Settings",
        "arabic_name": "Energy Point Settings",
        "link": "/app/energy-point-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Scorecard Criteria",
        "arabic_name": "Supplier Scorecard Criteria",
        "link": "/app/supplier-scorecard-criteria"
    },
    {
        "Type": "doctype",
        "english_name": "Error Snapshot",
        "arabic_name": "Error Snapshot",
        "link": "/app/error-snapshot"
    },
    {
        "Type": "doctype",
        "english_name": "View Log",
        "arabic_name": "View Log",
        "link": "/app/view-log"
    },
    {
        "Type": "doctype",
        "english_name": "Print Format Field Template",
        "arabic_name": "Print Format Field Template",
        "link": "/app/print-format-field-template"
    },
    {
        "Type": "doctype",
        "english_name": "UOM",
        "arabic_name": "UOM",
        "link": "/app/uom"
    },
    {
        "Type": "doctype",
        "english_name": "Support Settings",
        "arabic_name": "Support Settings",
        "link": "/app/support-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Network Printer Settings",
        "arabic_name": "Network Printer Settings",
        "link": "/app/network-printer-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Discussion Topic",
        "arabic_name": "Discussion Topic",
        "link": "/app/discussion-topic"
    },
    {
        "Type": "doctype",
        "english_name": "Discussion Reply",
        "arabic_name": "Discussion Reply",
        "link": "/app/discussion-reply"
    },
    {
        "Type": "doctype",
        "english_name": "SMS Settings",
        "arabic_name": "SMS Settings",
        "link": "/app/sms-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Tag Link",
        "arabic_name": "Tag Link",
        "link": "/app/tag-link"
    },
    {
        "Type": "doctype",
        "english_name": "Note",
        "arabic_name": "Note",
        "link": "/app/note"
    },
    {
        "Type": "doctype",
        "english_name": "Print Settings",
        "arabic_name": "Print Settings",
        "link": "/app/print-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Party Specific Item",
        "arabic_name": "Party Specific Item",
        "link": "/app/party-specific-item"
    },
    {
        "Type": "doctype",
        "english_name": "Package Import",
        "arabic_name": "Package Import",
        "link": "/app/package-import"
    },
    {
        "Type": "doctype",
        "english_name": "Package Release",
        "arabic_name": "Package Release",
        "link": "/app/package-release"
    },
    {
        "Type": "doctype",
        "english_name": "Package",
        "arabic_name": "Package",
        "link": "/app/package"
    },
    {
        "Type": "doctype",
        "english_name": "Party Link",
        "arabic_name": "Party Link",
        "link": "/app/party-link"
    },
    {
        "Type": "doctype",
        "english_name": "Product Tax Category",
        "arabic_name": "Product Tax Category",
        "link": "/app/product-tax-category"
    },
    {
        "Type": "doctype",
        "english_name": "Item Review",
        "arabic_name": "Item Review",
        "link": "/app/item-review"
    },
    {
        "Type": "doctype",
        "english_name": "Tax Withholding Category",
        "arabic_name": "Tax Withholding Category",
        "link": "/app/tax-withholding-category"
    },
    {
        "Type": "doctype",
        "english_name": "Assignment Rule",
        "arabic_name": "Assignment Rule",
        "link": "/app/assignment-rule"
    },
    {
        "Type": "doctype",
        "english_name": "South Africa VAT Settings",
        "arabic_name": "South Africa VAT Settings",
        "link": "/app/south-africa-vat-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Wishlist",
        "arabic_name": "Wishlist",
        "link": "/app/wishlist"
    },
    {
        "Type": "doctype",
        "english_name": "Campaign",
        "arabic_name": "Campaign",
        "link": "/app/campaign"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Security Pledge",
        "arabic_name": "Loan Security Pledge",
        "link": "/app/loan-security-pledge"
    },
    {
        "Type": "doctype",
        "english_name": "Blanket Order",
        "arabic_name": "Blanket Order",
        "link": "/app/blanket-order"
    },
    {
        "Type": "doctype",
        "english_name": "Tax Rule",
        "arabic_name": "Tax Rule",
        "link": "/app/tax-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Maintenance Schedule",
        "arabic_name": "Maintenance Schedule",
        "link": "/app/maintenance-schedule"
    },
    {
        "Type": "doctype",
        "english_name": "Stock Entry Type",
        "arabic_name": "Stock Entry Type",
        "link": "/app/stock-entry-type"
    },
    {
        "Type": "doctype",
        "english_name": "Slack Webhook URL",
        "arabic_name": "Slack Webhook URL",
        "link": "/app/slack-webhook-url"
    },
    {
        "Type": "doctype",
        "english_name": "Promotional Scheme",
        "arabic_name": "Promotional Scheme",
        "link": "/app/promotional-scheme"
    },
    {
        "Type": "doctype",
        "english_name": "OAuth Authorization Code",
        "arabic_name": "OAuth Authorization Code",
        "link": "/app/oauth-authorization-code"
    },
    {
        "Type": "doctype",
        "english_name": "Import Supplier Invoice",
        "arabic_name": "Import Supplier Invoice",
        "link": "/app/import-supplier-invoice"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Application",
        "arabic_name": "Loan Application",
        "link": "/app/loan-application"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Security Unpledge",
        "arabic_name": "Loan Security Unpledge",
        "link": "/app/loan-security-unpledge"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Write Off",
        "arabic_name": "Loan Write Off",
        "link": "/app/loan-write-off"
    },
    {
        "Type": "doctype",
        "english_name": "Subscription",
        "arabic_name": "Subscription",
        "link": "/app/subscription"
    },
    {
        "Type": "doctype",
        "english_name": "POS Settings",
        "arabic_name": "POS Settings",
        "link": "/app/pos-settings"
    },
    {
        "Type": "doctype",
        "english_name": "User Group",
        "arabic_name": "User Group",
        "link": "/app/user-group"
    },
    {
        "Type": "doctype",
        "english_name": "Social Media Post",
        "arabic_name": "Social Media Post",
        "link": "/app/social-media-post"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": ''' {
        "Type": "doctype",
        "english_name": "Contact Us Settings",
        "arabic_name": "Contact Us Settings",
        "link": "/app/contact-us-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Plaid Settings",
        "arabic_name": "Plaid Settings",
        "link": "/app/plaid-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Mpesa Settings",
        "arabic_name": "Mpesa Settings",
        "link": "/app/mpesa-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Brand",
        "arabic_name": "Brand",
        "link": "/app/brand"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Meeting",
        "arabic_name": "Quality Meeting",
        "link": "/app/quality-meeting"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Category",
        "arabic_name": "Asset Category",
        "link": "/app/asset-category"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Inspection Parameter",
        "arabic_name": "Quality Inspection Parameter",
        "link": "/app/quality-inspection-parameter"
    },
    {
        "Type": "doctype",
        "english_name": "LinkedIn Settings",
        "arabic_name": "LinkedIn Settings",
        "link": "/app/linkedin-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Twitter Settings",
        "arabic_name": "Twitter Settings",
        "link": "/app/twitter-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Homepage",
        "arabic_name": "Homepage",
        "link": "/app/homepage"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Term",
        "arabic_name": "Payment Term",
        "link": "/app/payment-term"
    },
    {
        "Type": "doctype",
        "english_name": "Accounting Dimension",
        "arabic_name": "Accounting Dimension",
        "link": "/app/accounting-dimension"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Inspection Parameter Group",
        "arabic_name": "Quality Inspection Parameter Group",
        "link": "/app/quality-inspection-parameter-group"
    },
    {
        "Type": "doctype",
        "english_name": "Accounting Dimension Filter",
        "arabic_name": "Accounting Dimension Filter",
        "link": "/app/accounting-dimension-filter"
    },
    {
        "Type": "doctype",
        "english_name": "Auto Email Report",
        "arabic_name": "Auto Email Report",
        "link": "/app/auto-email-report"
    },
    {
        "Type": "doctype",
        "english_name": "Landed Cost Voucher",
        "arabic_name": "Landed Cost Voucher",
        "link": "/app/landed-cost-voucher"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Maintenance Team",
        "arabic_name": "Asset Maintenance Team",
        "link": "/app/asset-maintenance-team"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Value Adjustment",
        "arabic_name": "Asset Value Adjustment",
        "link": "/app/asset-value-adjustment"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Maintenance Log",
        "arabic_name": "Asset Maintenance Log",
        "link": "/app/asset-maintenance-log"
    },
    {
        "Type": "doctype",
        "english_name": "Website Theme",
        "arabic_name": "Website Theme",
        "link": "/app/website-theme"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Security Price",
        "arabic_name": "Loan Security Price",
        "link": "/app/loan-security-price"
    },
    {
        "Type": "doctype",
        "english_name": "Process Loan Security Shortfall",
        "arabic_name": "Process Loan Security Shortfall",
        "link": "/app/process-loan-security-shortfall"
    },
    {
        "Type": "doctype",
        "english_name": "Auto Repeat",
        "arabic_name": "Auto Repeat",
        "link": "/app/auto-repeat"
    },
    {
        "Type": "doctype",
        "english_name": "UAE VAT Settings",
        "arabic_name": "UAE VAT Settings",
        "link": "/app/uae-vat-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Workflow",
        "arabic_name": "Workflow",
        "link": "/app/workflow"
    },
    {
        "Type": "doctype",
        "english_name": "Voice Call Settings",
        "arabic_name": "Voice Call Settings",
        "link": "/app/voice-call-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Contract",
        "arabic_name": "Contract",
        "link": "/app/contract"
    },
    {
        "Type": "doctype",
        "english_name": "Contract Template",
        "arabic_name": "Contract Template",
        "link": "/app/contract-template"
    },
    {
        "Type": "doctype",
        "english_name": "Custom DocPerm",
        "arabic_name": "Custom DocPerm",
        "link": "/app/custom-docperm"
    },
    {
        "Type": "doctype",
        "english_name": "Putaway Rule",
        "arabic_name": "Putaway Rule",
        "link": "/app/putaway-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Incoming Call Settings",
        "arabic_name": "Incoming Call Settings",
        "link": "/app/incoming-call-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Communication Medium",
        "arabic_name": "Communication Medium",
        "link": "/app/communication-medium"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Action",
        "arabic_name": "Quality Action",
        "link": "/app/quality-action"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Feedback",
        "arabic_name": "Quality Feedback",
        "link": "/app/quality-feedback"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Feedback Template",
        "arabic_name": "Quality Feedback Template",
        "link": "/app/quality-feedback-template"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Quality Goal",
        "arabic_name": "Quality Goal",
        "link": "/app/quality-goal"
    },
    {
        "Type": "doctype",
        "english_name": "Event Producer Last Update",
        "arabic_name": "Event Producer Last Update",
        "link": "/app/event-producer-last-update"
    },
    {
        "Type": "doctype",
        "english_name": "Event Producer",
        "arabic_name": "Event Producer",
        "link": "/app/event-producer"
    },
    {
        "Type": "doctype",
        "english_name": "Loan Security",
        "arabic_name": "Loan Security",
        "link": "/app/loan-security"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Review",
        "arabic_name": "Quality Review",
        "link": "/app/quality-review"
    },
    {
        "Type": "doctype",
        "english_name": "About Us Settings",
        "arabic_name": "About Us Settings",
        "link": "/app/about-us-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Item Attribute",
        "arabic_name": "Item Attribute",
        "link": "/app/item-attribute"
    },
    {
        "Type": "doctype",
        "english_name": "Social Login Key",
        "arabic_name": "Social Login Key",
        "link": "/app/social-login-key"
    },
    {
        "Type": "doctype",
        "english_name": "Blog Category",
        "arabic_name": "Blog Category",
        "link": "/app/blog-category"
    },
    {
        "Type": "doctype",
        "english_name": "Shipment Parcel Template",
        "arabic_name": "Shipment Parcel Template",
        "link": "/app/shipment-parcel-template"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Gateway Account",
        "arabic_name": "Payment Gateway Account",
        "link": "/app/payment-gateway-account"
    },
    {
        "Type": "doctype",
        "english_name": "Mode of Payment",
        "arabic_name": "Mode of Payment",
        "link": "/app/mode-of-payment"
    },
    {
        "Type": "doctype",
        "english_name": "Domain",
        "arabic_name": "Domain",
        "link": "/app/domain"
    },
    {
        "Type": "doctype",
        "english_name": "Calendar View",
        "arabic_name": "Calendar View",
        "link": "/app/calendar-view"
    },
    {
        "Type": "doctype",
        "english_name": "Google Contacts",
        "arabic_name": "Google Contacts",
        "link": "/app/google-contacts"
    },
    {
        "Type": "doctype",
        "english_name": "Document Follow",
        "arabic_name": "Document Follow",
        "link": "/app/document-follow"
    },
    {
        "Type": "doctype",
        "english_name": "Event Consumer",
        "arabic_name": "Event Consumer",
        "link": "/app/event-consumer"
    },
    {
        "Type": "doctype",
        "english_name": "Video",
        "arabic_name": "Video",
        "link": "/app/video"
    },
    {
        "Type": "doctype",
        "english_name": "Video Settings",
        "arabic_name": "Video Settings",
        "link": "/app/video-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Event Update Log",
        "arabic_name": "Event Update Log",
        "link": "/app/event-update-log"
    },
    {
        "Type": "doctype",
        "english_name": "Process Deferred Accounting",
        "arabic_name": "Process Deferred Accounting",
        "link": "/app/process-deferred-accounting"
    },
    {
        "Type": "doctype",
        "english_name": "Email Digest",
        "arabic_name": "Email Digest",
        "link": "/app/email-digest"
    },
    {
        "Type": "doctype",
        "english_name": "Navbar Settings",
        "arabic_name": "Navbar Settings",
        "link": "/app/navbar-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Portal Settings",
        "arabic_name": "Portal Settings",
        "link": "/app/portal-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Dunning",
        "arabic_name": "Dunning",
        "link": "/app/dunning"
    },
    {
        "Type": "doctype",
        "english_name": "Dashboard",
        "arabic_name": "Dashboard",
        "link": "/app/dashboard"
    },
    {
        "Type": "doctype",
        "english_name": "Bank",
        "arabic_name": "Bank",
        "link": "/app/bank"
    },
    {
        "Type": "doctype",
        "english_name": "Dunning Type",
        "arabic_name": "Dunning Type",
        "link": "/app/dunning-type"
    },
    {
        "Type": "doctype",
        "english_name": "Email Campaign",
        "arabic_name": "Email Campaign",
        "link": "/app/email-campaign"
    },
    {
        "Type": "doctype",
        "english_name": "Dashboard Chart Source",
        "arabic_name": "Dashboard Chart Source",
        "link": "/app/dashboard-chart-source"
    },
    {
        "Type": "doctype",
        "english_name": "Customs Tariff Number",
        "arabic_name": "Customs Tariff Number",
        "link": "/app/customs-tariff-number"
    },
    {
        "Type": "doctype",
        "english_name": "Subscription Settings",
        "arabic_name": "Subscription Settings",
        "link": "/app/subscription-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Module Onboarding",
        "arabic_name": "Module Onboarding",
        "link": "/app/module-onboarding"
    },
    {
        "Type": "doctype",
        "english_name": "POS Opening Entry",
        "arabic_name": "POS Opening Entry",
        "link": "/app/pos-opening-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Asset Maintenance",
        "arabic_name": "Asset Maintenance",
        "link": "/app/asset-maintenance"
    },
    {
        "Type": "doctype",
        "english_name": "Blogger",
        "arabic_name": "Blogger",
        "link": "/app/blogger"
    },
    {
        "Type": "doctype",
        "english_name": "Downtime Entry",
        "arabic_name": "Downtime Entry",
        "link": "/app/downtime-entry"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Loan Security Type",
        "arabic_name": "Loan Security Type",
        "link": "/app/loan-security-type"
    },
    {
        "Type": "doctype",
        "english_name": "List View Settings",
        "arabic_name": "List View Settings",
        "link": "/app/list-view-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Installed Applications",
        "arabic_name": "Installed Applications",
        "link": "/app/installed-applications"
    },
    {
        "Type": "doctype",
        "english_name": "Journal Entry Template",
        "arabic_name": "Journal Entry Template",
        "link": "/app/journal-entry-template"
    },
    {
        "Type": "doctype",
        "english_name": "Tally Migration",
        "arabic_name": "Tally Migration",
        "link": "/app/tally-migration"
    },
    {
        "Type": "doctype",
        "english_name": "Quality Inspection Template",
        "arabic_name": "Quality Inspection Template",
        "link": "/app/quality-inspection-template"
    },
    {
        "Type": "doctype",
        "english_name": "Project Template",
        "arabic_name": "Project Template",
        "link": "/app/project-template"
    },
    {
        "Type": "doctype",
        "english_name": "Color",
        "arabic_name": "Color",
        "link": "/app/color"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Account Type",
        "arabic_name": "Bank Account Type",
        "link": "/app/bank-account-type"
    },
    {
        "Type": "doctype",
        "english_name": "Item Manufacturer",
        "arabic_name": "Item Manufacturer",
        "link": "/app/item-manufacturer"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Order",
        "arabic_name": "Payment Order",
        "link": "/app/payment-order"
    },
    {
        "Type": "doctype",
        "english_name": "Payment Terms Template",
        "arabic_name": "Payment Terms Template",
        "link": "/app/payment-terms-template"
    },
    {
        "Type": "doctype",
        "english_name": "Dashboard Settings",
        "arabic_name": "Dashboard Settings",
        "link": "/app/dashboard-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Person",
        "arabic_name": "Sales Person",
        "link": "/app/sales-person"
    },
    {
        "Type": "doctype",
        "english_name": "Chart of Accounts Importer",
        "arabic_name": "Chart of Accounts Importer",
        "link": "/app/chart-of-accounts-importer"
    },
    {
        "Type": "doctype",
        "english_name": "Sanctioned Loan Amount",
        "arabic_name": "Sanctioned Loan Amount",
        "link": "/app/sanctioned-loan-amount"
    },
    {
        "Type": "doctype",
        "english_name": "Loyalty Point Entry",
        "arabic_name": "Loyalty Point Entry",
        "link": "/app/loyalty-point-entry"
    },
    {
        "Type": "doctype",
        "english_name": "Share Transfer",
        "arabic_name": "Share Transfer",
        "link": "/app/share-transfer"
    },
    {
        "Type": "doctype",
        "english_name": "Website Route Meta",
        "arabic_name": "Website Route Meta",
        "link": "/app/website-route-meta"
    },
    {
        "Type": "doctype",
        "english_name": "Woocommerce Settings",
        "arabic_name": "Woocommerce Settings",
        "link": "/app/woocommerce-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Energy Point Rule",
        "arabic_name": "Energy Point Rule",
        "link": "/app/energy-point-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Coupon Code",
        "arabic_name": "Coupon Code",
        "link": "/app/coupon-code"
    },
    {
        "Type": "doctype",
        "english_name": "Sales Partner",
        "arabic_name": "Sales Partner",
        "link": "/app/sales-partner"
    },
    {
        "Type": "doctype",
        "english_name": "Global Search Settings",
        "arabic_name": "Global Search Settings",
        "link": "/app/global-search-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Document Type Mapping",
        "arabic_name": "Document Type Mapping",
        "link": "/app/document-type-mapping"
    },
    {
        "Type": "doctype",
        "english_name": "Event Sync Log",
        "arabic_name": "Event Sync Log",
        "link": "/app/event-sync-log"
    },
    {
        "Type": "doctype",
        "english_name": "Quick Stock Balance",
        "arabic_name": "Quick Stock Balance",
        "link": "/app/quick-stock-balance"
    },
    {
        "Type": "doctype",
        "english_name": "Tag",
        "arabic_name": "Tag",
        "link": "/app/tag"
    },
    {
        "Type": "doctype",
        "english_name": "Custom Role",
        "arabic_name": "Custom Role",
        "link": "/app/custom-role"
    },
    {
        "Type": "doctype",
        "english_name": "List Filter",
        "arabic_name": "List Filter",
        "link": "/app/list-filter"
    },
    {
        "Type": "doctype",
        "english_name": "Success Action",
        "arabic_name": "Success Action",
        "link": "/app/success-action"
    },
    {
        "Type": "doctype",
        "english_name": "Transaction Log",
        "arabic_name": "Transaction Log",
        "link": "/app/transaction-log"
    },
    {
        "Type": "doctype",
        "english_name": "Email Unsubscribe",
        "arabic_name": "Email Unsubscribe",
        "link": "/app/email-unsubscribe"
    },
    {
        "Type": "doctype",
        "english_name": "Google Calendar",
        "arabic_name": "Google Calendar",
        "link": "/app/google-calendar"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''{
        "Type": "doctype",
        "english_name": "QuickBooks Migrator",
        "arabic_name": "QuickBooks Migrator",
        "link": "/app/quickbooks-migrator"
    },
    {
        "Type": "doctype",
        "english_name": "Accounting Period",
        "arabic_name": "Accounting Period",
        "link": "/app/accounting-period"
    },
    {
        "Type": "doctype",
        "english_name": "Session Default Settings",
        "arabic_name": "Session Default Settings",
        "link": "/app/session-default-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Manufacturer",
        "arabic_name": "Manufacturer",
        "link": "/app/manufacturer"
    },
    {
        "Type": "doctype",
        "english_name": "Issue Type",
        "arabic_name": "Issue Type",
        "link": "/app/issue-type"
    },
    {
        "Type": "doctype",
        "english_name": "Price List",
        "arabic_name": "Price List",
        "link": "/app/price-list"
    },
    {
        "Type": "doctype",
        "english_name": "Invoice Discounting",
        "arabic_name": "Invoice Discounting",
        "link": "/app/invoice-discounting"
    },
    {
        "Type": "doctype",
        "english_name": "Warehouse Type",
        "arabic_name": "Warehouse Type",
        "link": "/app/warehouse-type"
    },
    {
        "Type": "doctype",
        "english_name": "Loyalty Program",
        "arabic_name": "Loyalty Program",
        "link": "/app/loyalty-program"
    },
    {
        "Type": "doctype",
        "english_name": "Shipping Rule",
        "arabic_name": "Shipping Rule",
        "link": "/app/shipping-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Exotel Settings",
        "arabic_name": "Exotel Settings",
        "link": "/app/exotel-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Issue Priority",
        "arabic_name": "Issue Priority",
        "link": "/app/issue-priority"
    },
    {
        "Type": "doctype",
        "english_name": "Personal Data Download Request",
        "arabic_name": "Personal Data Download Request",
        "link": "/app/personal-data-download-request"
    },
    {
        "Type": "doctype",
        "english_name": "Milestone Tracker",
        "arabic_name": "Milestone Tracker",
        "link": "/app/milestone-tracker"
    },
    {
        "Type": "doctype",
        "english_name": "Milestone",
        "arabic_name": "Milestone",
        "link": "/app/milestone"
    },
    {
        "Type": "doctype",
        "english_name": "Homepage Section",
        "arabic_name": "Homepage Section",
        "link": "/app/homepage-section"
    },
    {
        "Type": "doctype",
        "english_name": "Website Slideshow",
        "arabic_name": "Website Slideshow",
        "link": "/app/website-slideshow"
    },
    {
        "Type": "doctype",
        "english_name": "Activity Cost",
        "arabic_name": "Activity Cost",
        "link": "/app/activity-cost"
    },
    {
        "Type": "doctype",
        "english_name": "Role Permission for Page and Report",
        "arabic_name": "Role Permission for Page and Report",
        "link": "/app/role-permission-for-page-and-report"
    },
    {
        "Type": "doctype",
        "english_name": "Desktop Icon",
        "arabic_name": "Desktop Icon",
        "link": "/app/desktop-icon"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Scorecard Period",
        "arabic_name": "Supplier Scorecard Period",
        "link": "/app/supplier-scorecard-period"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Scorecard Variable",
        "arabic_name": "Supplier Scorecard Variable",
        "link": "/app/supplier-scorecard-variable"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Scorecard",
        "arabic_name": "Supplier Scorecard",
        "link": "/app/supplier-scorecard"
    },
    {
        "Type": "doctype",
        "english_name": "Supplier Scorecard Standing",
        "arabic_name": "Supplier Scorecard Standing",
        "link": "/app/supplier-scorecard-standing"
    },
    {
        "Type": "doctype",
        "english_name": "Project Update",
        "arabic_name": "Project Update",
        "link": "/app/project-update"
    },
    {
        "Type": "doctype",
        "english_name": "Employee Group",
        "arabic_name": "Employee Group",
        "link": "/app/employee-group"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Account Subtype",
        "arabic_name": "Bank Account Subtype",
        "link": "/app/bank-account-subtype"
    },
    {
        "Type": "doctype",
        "english_name": "Market Segment",
        "arabic_name": "Market Segment",
        "link": "/app/market-segment"
    },
    {
        "Type": "doctype",
        "english_name": "Delivery Settings",
        "arabic_name": "Delivery Settings",
        "link": "/app/delivery-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Email Rule",
        "arabic_name": "Email Rule",
        "link": "/app/email-rule"
    },
    {
        "Type": "doctype",
        "english_name": "Bank Guarantee",
        "arabic_name": "Bank Guarantee",
        "link": "/app/bank-guarantee"
    },
    {
        "Type": "doctype",
        "english_name": "UOM Conversion Factor",
        "arabic_name": "UOM Conversion Factor",
        "link": "/app/uom-conversion-factor"
    },
    {
        "Type": "doctype",
        "english_name": "SMS Log",
        "arabic_name": "SMS Log",
        "link": "/app/sms-log"
    },
    {
        "Type": "doctype",
        "english_name": "Installation Note",
        "arabic_name": "Installation Note",
        "link": "/app/installation-note"
    },
    {
        "Type": "doctype",
        "english_name": "Routing",
        "arabic_name": "Routing",
        "link": "/app/routing"
    },
    {
        "Type": "doctype",
        "english_name": "Share Type",
        "arabic_name": "Share Type",
        "link": "/app/share-type"
    },
    {
        "Type": "doctype",
        "english_name": "BOM Update Tool",
        "arabic_name": "BOM Update Tool",
        "link": "/app/bom-update-tool"
    },
    {
        "Type": "doctype",
        "english_name": "Item Alternative",
        "arabic_name": "Item Alternative",
        "link": "/app/item-alternative"
    },
    {
        "Type": "doctype",
        "english_name": "Currency Exchange",
        "arabic_name": "Currency Exchange",
        "link": "/app/currency-exchange"
    },
    {
        "Type": "doctype",
        "english_name": "Finance Book",
        "arabic_name": "Finance Book",
        "link": "/app/finance-book"
    },
    {
        "Type": "doctype",
        "english_name": "UOM Category",
        "arabic_name": "UOM Category",
        "link": "/app/uom-category"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''   {
        "Type": "doctype",
        "english_name": "Party Type",
        "arabic_name": "Party Type",
        "link": "/app/party-type"
    },
    {
        "Type": "doctype",
        "english_name": "Version",
        "arabic_name": "Version",
        "link": "/app/version"
    },
    {
        "Type": "doctype",
        "english_name": "Data Export",
        "arabic_name": "Data Export",
        "link": "/app/data-export"
    },
    {
        "Type": "doctype",
        "english_name": "Projects Settings",
        "arabic_name": "Projects Settings",
        "link": "/app/projects-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Item Variant Settings",
        "arabic_name": "Item Variant Settings",
        "link": "/app/item-variant-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Cash Flow Mapper",
        "arabic_name": "Cash Flow Mapper",
        "link": "/app/cash-flow-mapper"
    },
    {
        "Type": "doctype",
        "english_name": "Cash Flow Mapping",
        "arabic_name": "Cash Flow Mapping",
        "link": "/app/cash-flow-mapping"
    },
    {
        "Type": "doctype",
        "english_name": "GoCardless Mandate",
        "arabic_name": "GoCardless Mandate",
        "link": "/app/gocardless-mandate"
    },
    {
        "Type": "doctype",
        "english_name": "Cash Flow Mapping Template",
        "arabic_name": "Cash Flow Mapping Template",
        "link": "/app/cash-flow-mapping-template"
    },
    {
        "Type": "doctype",
        "english_name": "Domain Settings",
        "arabic_name": "Domain Settings",
        "link": "/app/domain-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Opportunity Type",
        "arabic_name": "Opportunity Type",
        "link": "/app/opportunity-type"
    },
    {
        "Type": "doctype",
        "english_name": "Page",
        "arabic_name": "Page",
        "link": "/app/page"
    },
    {
        "Type": "doctype",
        "english_name": "SMS Center",
        "arabic_name": "SMS Center",
        "link": "/app/sms-center"
    },
    {
        "Type": "doctype",
        "english_name": "Unhandled Email",
        "arabic_name": "Unhandled Email",
        "link": "/app/unhandled-email"
    },
    {
        "Type": "doctype",
        "english_name": "Print Style",
        "arabic_name": "Print Style",
        "link": "/app/print-style"
    },
    {
        "Type": "doctype",
        "english_name": "Project Type",
        "arabic_name": "Project Type",
        "link": "/app/project-type"
    },
    {
        "Type": "doctype",
        "english_name": "Activity Type",
        "arabic_name": "Activity Type",
        "link": "/app/activity-type"
    },
    {
        "Type": "doctype",
        "english_name": "Address Template",
        "arabic_name": "Address Template",
        "link": "/app/address-template"
    },
    {
        "Type": "doctype",
        "english_name": "Website Script",
        "arabic_name": "Website Script",
        "link": "/app/website-script"
    },
    {
        "Type": "doctype",
        "english_name": "Bulk Update",
        "arabic_name": "Bulk Update",
        "link": "/app/bulk-update"
    },
    {
        "Type": "doctype",
        "english_name": "OAuth Provider Settings",
        "arabic_name": "OAuth Provider Settings",
        "link": "/app/oauth-provider-settings"
    },
    {
        "Type": "doctype",
        "english_name": "Help Category",
        "arabic_name": "Help Category",
        "link": "/app/help-category"
    },
    {
        "Type": "doctype",
        "english_name": "Website Sidebar",
        "arabic_name": "Website Sidebar",
        "link": "/app/website-sidebar"
    },
    {
        "Type": "doctype",
        "english_name": "Monthly Distribution",
        "arabic_name": "Monthly Distribution",
        "link": "/app/monthly-distribution"
    },
    {
        "Type": "doctype",
        "english_name": "Branch",
        "arabic_name": "Branch",
        "link": "/app/branch"
    },
    {
        "Type": "doctype",
        "english_name": "Cheque Print Template",
        "arabic_name": "Cheque Print Template",
        "link": "/app/cheque-print-template"
    },
    {
        "Type": "doctype",
        "english_name": "Rename Tool",
        "arabic_name": "Rename Tool",
        "link": "/app/rename-tool"
    },
    {
        "Type": "doctype",
        "english_name": "Authorization Control",
        "arabic_name": "Authorization Control",
        "link": "/app/authorization-control"
    },
    {
        "Type": "page",
        "english_name": "activity",
        "arabic_name": "activity",
        "link": "/app/activity"
    },
    {
        "Type": "page",
        "english_name": "permission-manager",
        "arabic_name": "permission-manager",
        "link": "/app/permission-manager"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": ''' {
        "Type": "page",
        "english_name": "sales-funnel",
        "arabic_name": "sales-funnel",
        "link": "/app/sales-funnel"
    },
    {
        "Type": "page",
        "english_name": "backups",
        "arabic_name": "backups",
        "link": "/app/backups"
    },
    {
        "Type": "page",
        "english_name": "stock-balance",
        "arabic_name": "stock-balance",
        "link": "/app/stock-balance"
    },
    {
        "Type": "page",
        "english_name": "background_jobs",
        "arabic_name": "background_jobs",
        "link": "/app/background_jobs"
    },
    {
        "Type": "page",
        "english_name": "print-format-builder",
        "arabic_name": "print-format-builder",
        "link": "/app/print-format-builder"
    },
    {
        "Type": "page",
        "english_name": "recorder",
        "arabic_name": "recorder",
        "link": "/app/recorder"
    },
    {
        "Type": "page",
        "english_name": "bom-comparison-tool",
        "arabic_name": "bom-comparison-tool",
        "link": "/app/bom-comparison-tool"
    },
    {
        "Type": "page",
        "english_name": "leaderboard",
        "arabic_name": "leaderboard",
        "link": "/app/leaderboard"
    },
    {
        "Type": "page",
        "english_name": "user-profile",
        "arabic_name": "user-profile",
        "link": "/app/user-profile"
    },
    {
        "Type": "page",
        "english_name": "point-of-sale",
        "arabic_name": "point-of-sale",
        "link": "/app/point-of-sale"
    },
    {
        "Type": "page",
        "english_name": "print",
        "arabic_name": "print",
        "link": "/app/print"
    },
    {
        "Type": "page",
        "english_name": "warehouse-capacity-summary",
        "arabic_name": "warehouse-capacity-summary",
        "link": "/app/warehouse-capacity-summary"
    },
    {
        "Type": "page",
        "english_name": "dashboard-view",
        "arabic_name": "dashboard-view",
        "link": "/app/dashboard-view"
    },
    {
        "Type": "page",
        "english_name": "print-format-builder-beta",
        "arabic_name": "print-format-builder-beta",
        "link": "/app/print-format-builder-beta"
    },
    {
        "Type": "page",
        "english_name": "doppio-bot",
        "arabic_name": "doppio-bot",
        "link": "/app/doppio-bot"
    },
    {
        "Type": "page",
        "english_name": "product_e",
        "arabic_name": "product_e",
        "link": "/app/product_e"
    },
    {
        "Type": "page",
        "english_name": "setup-wizard",
        "arabic_name": "setup-wizard",
        "link": "/app/setup-wizard"
    },
    {
        "Type": "page",
        "english_name": "ai_interface",
        "arabic_name": "ai_interface",
        "link": "/app/ai_interface"
    },
    {
        "Type": "Workspace",
        "english_name": "LOGO-Administrator",
        "arabic_name": "LOGO-Administrator",
        "link": "/app/logo-administrator"
    },
    {
        "Type": "Workspace",
        "english_name": "Accounting",
        "arabic_name": "Accounting",
        "link": "/app/accounting"
    },
    {
        "Type": "Workspace",
        "english_name": "erpalfras Settings",
        "arabic_name": "erpalfras Settings",
        "link": "/app/erpalfras-settings"
    },
    {
        "Type": "Workspace",
        "english_name": "Settings",
        "arabic_name": "Settings",
        "link": "/app/settings"
    },
    {
        "Type": "Workspace",
        "english_name": "Loans",
        "arabic_name": "Loans",
        "link": "/app/loans"
    },
    {
        "Type": "Workspace",
        "english_name": "Welcome Workspace",
        "arabic_name": "Welcome Workspace",
        "link": "/app/welcome-workspace"
    },
    {
        "Type": "Workspace",
        "english_name": "Manufacturing",
        "arabic_name": "Manufacturing",
        "link": "/app/manufacturing"
    },
    {
        "Type": "Workspace",
        "english_name": "CRM",
        "arabic_name": "CRM",
        "link": "/app/crm"
    },
    {
        "Type": "Workspace",
        "english_name": "Selling",
        "arabic_name": "Selling",
        "link": "/app/selling"
    },
    {
        "Type": "Workspace",
        "english_name": "Integrations",
        "arabic_name": "Integrations",
        "link": "/app/integrations"
    },
    {
        "Type": "Workspace",
        "english_name": "erpalfras Integrations",
        "arabic_name": "erpalfras Integrations",
        "link": "/app/erpalfras-integrations"
    },
    {
        "Type": "Workspace",
        "english_name": "Tools",
        "arabic_name": "Tools",
        "link": "/app/tools"
    },
    {
        "Type": "Workspace",
        "english_name": "Build",
        "arabic_name": "Build",
        "link": "/app/build"
    },
    {
        "Type": "Workspace",
        "english_name": "Website",
        "arabic_name": "Website",
        "link": "/app/website"
    },
    {
        "Type": "Workspace",
        "english_name": "Users",
        "arabic_name": "Users",
        "link": "/app/users"
    },
    {
        "Type": "Workspace",
        "english_name": "Support",
        "arabic_name": "Support",
        "link": "/app/support"
    },
    {
        "Type": "Workspace",
        "english_name": "Projects",
        "arabic_name": "Projects",
        "link": "/app/projects"
    },
    {
        "Type": "Workspace",
        "english_name": "Quality",
        "arabic_name": "Quality",
        "link": "/app/quality"
    },
    {
        "Type": "Workspace",
        "english_name": "Stock",
        "arabic_name": "Stock",
        "link": "/app/stock"
    },
    {
        "Type": "Workspace",
        "english_name": "Buying",
        "arabic_name": "Buying",
        "link": "/app/buying"
    },
    {
        "Type": "Workspace",
        "english_name": "Assets",
        "arabic_name": "Assets",
        "link": "/app/assets"
    },
    {
        "Type": "Workspace",
        "english_name": "Home",
        "arabic_name": "Home",
        "link": "/app/home"
    },
    {
        "Type": "Report",
        "english_name": "KSA VAT",
        "arabic_name": "KSA VAT",
        "link": "/app/ksa-vat"
    },
    {
        "Type": "Report",
        "english_name": "KSA Report Ditals",
        "arabic_name": "KSA Report Ditals",
        "link": "/app/ksa-report-ditals"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''{
        "Type": "Report",
        "english_name": "VAT KSA Report",
        "arabic_name": "VAT KSA Report",
        "link": "/app/vat-ksa-report"
    },
    {
        "Type": "Report",
        "english_name": "Available Batch Report",
        "arabic_name": "Available Batch Report",
        "link": "/app/available-batch-report"
    },
    {
        "Type": "Report",
        "english_name": "Completed Work Orders",
        "arabic_name": "Completed Work Orders",
        "link": "/app/completed-work-orders"
    },
    {
        "Type": "Report",
        "english_name": "Lost Quotations",
        "arabic_name": "Lost Quotations",
        "link": "/app/lost-quotations"
    },
    {
        "Type": "Report",
        "english_name": "Asset Depreciation Ledger",
        "arabic_name": "Asset Depreciation Ledger",
        "link": "/app/asset-depreciation-ledger"
    },
    {
        "Type": "Report",
        "english_name": "Stock Ledger Variance",
        "arabic_name": "Stock Ledger Variance",
        "link": "/app/stock-ledger-variance"
    },
    {
        "Type": "Report",
        "english_name": "General and Payment Ledger Comparison",
        "arabic_name": "General and Payment Ledger Comparison",
        "link": "/app/general-and-payment-ledger-comparison"
    },
    {
        "Type": "Report",
        "english_name": "Asset Depreciations and Balances",
        "arabic_name": "Asset Depreciations and Balances",
        "link": "/app/asset-depreciations-and-balances"
    },
    {
        "Type": "Report",
        "english_name": "Fixed Asset Register",
        "arabic_name": "Fixed Asset Register",
        "link": "/app/fixed-asset-register"
    },
    {
        "Type": "Report",
        "english_name": "Voucher-wise Balance",
        "arabic_name": "Voucher-wise Balance",
        "link": "/app/voucher-wise-balance"
    },
    {
        "Type": "Report",
        "english_name": "Audit System Hooks",
        "arabic_name": "Audit System Hooks",
        "link": "/app/audit-system-hooks"
    },
    {
        "Type": "Report",
        "english_name": "Warehouse Wise Stock Balance",
        "arabic_name": "Warehouse Wise Stock Balance",
        "link": "/app/warehouse-wise-stock-balance"
    },
    {
        "Type": "Report",
        "english_name": "Database Storage Usage By Tables",
        "arabic_name": "Database Storage Usage By Tables",
        "link": "/app/database-storage-usage-by-tables"
    },
    {
        "Type": "Report",
        "english_name": "Payment Ledger",
        "arabic_name": "Payment Ledger",
        "link": "/app/payment-ledger"
    },
    {
        "Type": "Report",
        "english_name": "Lost Opportunity",
        "arabic_name": "Lost Opportunity",
        "link": "/app/lost-opportunity"
    },
    {
        "Type": "Report",
        "english_name": "FIFO Queue vs Qty After Transaction Comparison",
        "arabic_name": "FIFO Queue vs Qty After Transaction Comparison",
        "link": "/app/fifo-queue-vs-qty-after-transaction-comparison"
    },
    {
        "Type": "Report",
        "english_name": "Gross Profit",
        "arabic_name": "Gross Profit",
        "link": "/app/gross-profit"
    },
    {
        "Type": "Report",
        "english_name": "BOM Operations Time",
        "arabic_name": "BOM Operations Time",
        "link": "/app/bom-operations-time"
    },
    {
        "Type": "Report",
        "english_name": "Payment Terms Status for Sales Order",
        "arabic_name": "Payment Terms Status for Sales Order",
        "link": "/app/payment-terms-status-for-sales-order"
    },
    {
        "Type": "Report",
        "english_name": "Stock Ledger Invariant Check",
        "arabic_name": "Stock Ledger Invariant Check",
        "link": "/app/stock-ledger-invariant-check"
    },
    {
        "Type": "Report",
        "english_name": "Deferred Revenue and Expense",
        "arabic_name": "Deferred Revenue and Expense",
        "link": "/app/deferred-revenue-and-expense"
    },
    {
        "Type": "Report",
        "english_name": "Work Order Consumed Materials",
        "arabic_name": "Work Order Consumed Materials",
        "link": "/app/work-order-consumed-materials"
    },
    {
        "Type": "Report",
        "english_name": "Process Loss Report",
        "arabic_name": "Process Loss Report",
        "link": "/app/process-loss-report"
    },
    {
        "Type": "Report",
        "english_name": "Sales Partners Commission",
        "arabic_name": "Sales Partners Commission",
        "link": "/app/sales-partners-commission"
    },
    {
        "Type": "Report",
        "english_name": "TDS Computation Summary",
        "arabic_name": "TDS Computation Summary",
        "link": "/app/tds-computation-summary"
    },
    {
        "Type": "Report",
        "english_name": "TDS Payable Monthly",
        "arabic_name": "TDS Payable Monthly",
        "link": "/app/tds-payable-monthly"
    },
    {
        "Type": "Report",
        "english_name": "Opportunity Summary by Sales Stage",
        "arabic_name": "Opportunity Summary by Sales Stage",
        "link": "/app/opportunity-summary-by-sales-stage"
    },
    {
        "Type": "Report",
        "english_name": "VAT Audit Report",
        "arabic_name": "VAT Audit Report",
        "link": "/app/vat-audit-report"
    },
    {
        "Type": "Report",
        "english_name": "Sales Pipeline Analytics",
        "arabic_name": "Sales Pipeline Analytics",
        "link": "/app/sales-pipeline-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Incorrect Stock Value Report",
        "arabic_name": "Incorrect Stock Value Report",
        "link": "/app/incorrect-stock-value-report"
    },
    {
        "Type": "Report",
        "english_name": "COGS By Item Group",
        "arabic_name": "COGS By Item Group",
        "link": "/app/cogs-by-item-group"
    },
    {
        "Type": "Report",
        "english_name": "Subcontract Order Summary",
        "arabic_name": "Subcontract Order Summary",
        "link": "/app/subcontract-order-summary"
    },
    {
        "Type": "Report",
        "english_name": "Incorrect Serial No Valuation",
        "arabic_name": "Incorrect Serial No Valuation",
        "link": "/app/incorrect-serial-no-valuation"
    },
    {
        "Type": "Report",
        "english_name": "Incorrect Balance Qty After Transaction",
        "arabic_name": "Incorrect Balance Qty After Transaction",
        "link": "/app/incorrect-balance-qty-after-transaction"
    },
    {
        "Type": "Report",
        "english_name": "Serial No Ledger",
        "arabic_name": "Serial No Ledger",
        "link": "/app/serial-no-ledger"
    },
    {
        "Type": "Report",
        "english_name": "Delayed Tasks Summary",
        "arabic_name": "Delayed Tasks Summary",
        "link": "/app/delayed-tasks-summary"
    },
    {
        "Type": "Report",
        "english_name": "Dimension-wise Accounts Balance Report",
        "arabic_name": "Dimension-wise Accounts Balance Report",
        "link": "/app/dimension-wise-accounts-balance-report"
    },
    {
        "Type": "Report",
        "english_name": "Billed Items To Be Received",
        "arabic_name": "Billed Items To Be Received",
        "link": "/app/billed-items-to-be-received"
    },
    {
        "Type": "Report",
        "english_name": "Tax Detail",
        "arabic_name": "Tax Detail",
        "link": "/app/tax-detail"
    },
    {
        "Type": "Report",
        "english_name": "Loan Security Exposure",
        "arabic_name": "Loan Security Exposure",
        "link": "/app/loan-security-exposure"
    },
    {
        "Type": "Report",
        "english_name": "Applicant-Wise Loan Security Exposure",
        "arabic_name": "Applicant-Wise Loan Security Exposure",
        "link": "/app/applicant-wise-loan-security-exposure"
    },
    {
        "Type": "Report",
        "english_name": "Cost of Poor Quality Report",
        "arabic_name": "Cost of Poor Quality Report",
        "link": "/app/cost-of-poor-quality-report"
    },
    {
        "Type": "Report",
        "english_name": "Loan Interest Report",
        "arabic_name": "Loan Interest Report",
        "link": "/app/loan-interest-report"
    },
    {
        "Type": "Report",
        "english_name": "Job Card Summary",
        "arabic_name": "Job Card Summary",
        "link": "/app/job-card-summary"
    },
    {
        "Type": "Report",
        "english_name": "Production Plan Summary",
        "arabic_name": "Production Plan Summary",
        "link": "/app/production-plan-summary"
    },
    {
        "Type": "Report",
        "english_name": "Issue Summary",
        "arabic_name": "Issue Summary",
        "link": "/app/issue-summary"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''{
        "Type": "Report",
        "english_name": "Issue Analytics",
        "arabic_name": "Issue Analytics",
        "link": "/app/issue-analytics"
    },
    {
        "Type": "Report",
        "english_name": "POS Register",
        "arabic_name": "POS Register",
        "link": "/app/pos-register"
    },
    {
        "Type": "Report",
        "english_name": "UAE VAT 201",
        "arabic_name": "UAE VAT 201",
        "link": "/app/uae-vat-201"
    },
    {
        "Type": "Report",
        "english_name": "First Response Time for Opportunity",
        "arabic_name": "First Response Time for Opportunity",
        "link": "/app/first-response-time-for-opportunity"
    },
    {
        "Type": "Report",
        "english_name": "First Response Time for Issues",
        "arabic_name": "First Response Time for Issues",
        "link": "/app/first-response-time-for-issues"
    },
    {
        "Type": "Report",
        "english_name": "YouTube Interactions",
        "arabic_name": "YouTube Interactions",
        "link": "/app/youtube-interactions"
    },
    {
        "Type": "Report",
        "english_name": "Lead Details",
        "arabic_name": "Lead Details",
        "link": "/app/lead-details"
    },
    {
        "Type": "Report",
        "english_name": "Stock Qty vs Serial No Count",
        "arabic_name": "Stock Qty vs Serial No Count",
        "link": "/app/stock-qty-vs-serial-no-count"
    },
    {
        "Type": "Report",
        "english_name": "Requested Items to Order and Receive",
        "arabic_name": "Requested Items to Order and Receive",
        "link": "/app/requested-items-to-order-and-receive"
    },
    {
        "Type": "Report",
        "english_name": "Sales Analytics",
        "arabic_name": "Sales Analytics",
        "link": "/app/sales-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Sales Order Analysis",
        "arabic_name": "Sales Order Analysis",
        "link": "/app/sales-order-analysis"
    },
    {
        "Type": "Report",
        "english_name": "Purchase Order Analysis",
        "arabic_name": "Purchase Order Analysis",
        "link": "/app/purchase-order-analysis"
    },
    {
        "Type": "Report",
        "english_name": "Exponential Smoothing Forecasting",
        "arabic_name": "Exponential Smoothing Forecasting",
        "link": "/app/exponential-smoothing-forecasting"
    },
    {
        "Type": "Report",
        "english_name": "Item Shortage Report",
        "arabic_name": "Item Shortage Report",
        "link": "/app/item-shortage-report"
    },
    {
        "Type": "Report",
        "english_name": "Project Summary",
        "arabic_name": "Project Summary",
        "link": "/app/project-summary"
    },
    {
        "Type": "Report",
        "english_name": "Stock Balance",
        "arabic_name": "Stock Balance",
        "link": "/app/stock-balance"
    },
    {
        "Type": "Report",
        "english_name": "Quality Inspection Summary",
        "arabic_name": "Quality Inspection Summary",
        "link": "/app/quality-inspection-summary"
    },
    {
        "Type": "Report",
        "english_name": "Downtime Analysis",
        "arabic_name": "Downtime Analysis",
        "link": "/app/downtime-analysis"
    },
    {
        "Type": "Report",
        "english_name": "Work Order Summary",
        "arabic_name": "Work Order Summary",
        "link": "/app/work-order-summary"
    },
    {
        "Type": "Report",
        "english_name": "Website Analytics",
        "arabic_name": "Website Analytics",
        "link": "/app/website-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Production Planning Report",
        "arabic_name": "Production Planning Report",
        "link": "/app/production-planning-report"
    },
    {
        "Type": "Report",
        "english_name": "Loan Repayment and Closure",
        "arabic_name": "Loan Repayment and Closure",
        "link": "/app/loan-repayment-and-closure"
    },
    {
        "Type": "Report",
        "english_name": "Review",
        "arabic_name": "Review",
        "link": "/app/review"
    },
    {
        "Type": "Report",
        "english_name": "Territory-wise Sales",
        "arabic_name": "Territory-wise Sales",
        "link": "/app/territory-wise-sales"
    },
    {
        "Type": "Report",
        "english_name": "Stock and Account Value Comparison",
        "arabic_name": "Stock and Account Value Comparison",
        "link": "/app/stock-and-account-value-comparison"
    },
    {
        "Type": "Report",
        "english_name": "Item-wise Sales History",
        "arabic_name": "Item-wise Sales History",
        "link": "/app/item-wise-sales-history"
    },
    {
        "Type": "Report",
        "english_name": "Loan Security Status",
        "arabic_name": "Loan Security Status",
        "link": "/app/loan-security-status"
    },
    {
        "Type": "Report",
        "english_name": "Lead Conversion Time",
        "arabic_name": "Lead Conversion Time",
        "link": "/app/lead-conversion-time"
    },
    {
        "Type": "Report",
        "english_name": "Procurement Tracker",
        "arabic_name": "Procurement Tracker",
        "link": "/app/procurement-tracker"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''{
        "Type": "Report",
        "english_name": "Delayed Order Report",
        "arabic_name": "Delayed Order Report",
        "link": "/app/delayed-order-report"
    },
    {
        "Type": "Report",
        "english_name": "Delayed Item Report",
        "arabic_name": "Delayed Item Report",
        "link": "/app/delayed-item-report"
    },
    {
        "Type": "Report",
        "english_name": "Customer-wise Item Price",
        "arabic_name": "Customer-wise Item Price",
        "link": "/app/customer-wise-item-price"
    },
    {
        "Type": "Report",
        "english_name": "Project Billing Summary",
        "arabic_name": "Project Billing Summary",
        "link": "/app/project-billing-summary"
    },
    {
        "Type": "Report",
        "english_name": "Employee Billing Summary",
        "arabic_name": "Employee Billing Summary",
        "link": "/app/employee-billing-summary"
    },
    {
        "Type": "Report",
        "english_name": "BOM Explorer",
        "arabic_name": "BOM Explorer",
        "link": "/app/bom-explorer"
    },
    {
        "Type": "Report",
        "english_name": "Subcontracted Raw Materials To Be Transferred",
        "arabic_name": "Subcontracted Raw Materials To Be Transferred",
        "link": "/app/subcontracted-raw-materials-to-be-transferred"
    },
    {
        "Type": "Report",
        "english_name": "Subcontracted Item To Be Received",
        "arabic_name": "Subcontracted Item To Be Received",
        "link": "/app/subcontracted-item-to-be-received"
    },
    {
        "Type": "Report",
        "english_name": "Inactive Sales Items",
        "arabic_name": "Inactive Sales Items",
        "link": "/app/inactive-sales-items"
    },
    {
        "Type": "Report",
        "english_name": "Territory Target Variance Based On Item Group",
        "arabic_name": "Territory Target Variance Based On Item Group",
        "link": "/app/territory-target-variance-based-on-item-group"
    },
    {
        "Type": "Report",
        "english_name": "Sales Person Target Variance Based On Item Group",
        "arabic_name": "Sales Person Target Variance Based On Item Group",
        "link": "/app/sales-person-target-variance-based-on-item-group"
    },
    {
        "Type": "Report",
        "english_name": "Sales Partner Target Variance based on Item Group",
        "arabic_name": "Sales Partner Target Variance based on Item Group",
        "link": "/app/sales-partner-target-variance-based-on-item-group"
    },
    {
        "Type": "Report",
        "english_name": "Sales Partner Transaction Summary",
        "arabic_name": "Sales Partner Transaction Summary",
        "link": "/app/sales-partner-transaction-summary"
    },
    {
        "Type": "Report",
        "english_name": "Share Ledger",
        "arabic_name": "Share Ledger",
        "link": "/app/share-ledger"
    },
    {
        "Type": "Report",
        "english_name": "Campaign Efficiency",
        "arabic_name": "Campaign Efficiency",
        "link": "/app/campaign-efficiency"
    },
    {
        "Type": "Report",
        "english_name": "Sales Partner Commission Summary",
        "arabic_name": "Sales Partner Commission Summary",
        "link": "/app/sales-partner-commission-summary"
    },
    {
        "Type": "Report",
        "english_name": "Product Bundle Balance",
        "arabic_name": "Product Bundle Balance",
        "link": "/app/product-bundle-balance"
    },
    {
        "Type": "Report",
        "english_name": "Purchase Analytics",
        "arabic_name": "Purchase Analytics",
        "link": "/app/purchase-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Stock Analytics",
        "arabic_name": "Stock Analytics",
        "link": "/app/stock-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Production Analytics",
        "arabic_name": "Production Analytics",
        "link": "/app/production-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Supplier Ledger Summary",
        "arabic_name": "Supplier Ledger Summary",
        "link": "/app/supplier-ledger-summary"
    },
    {
        "Type": "Report",
        "english_name": "Gross and Net Profit Report",
        "arabic_name": "Gross and Net Profit Report",
        "link": "/app/gross-and-net-profit-report"
    },
    {
        "Type": "Report",
        "english_name": "Trial Balance (Simple)",
        "arabic_name": "Trial Balance (Simple)",
        "link": "/app/trial-balance-(simple)"
    },
    {
        "Type": "Report",
        "english_name": "IRS 1099",
        "arabic_name": "IRS 1099",
        "link": "/app/irs-1099"
    },
    {
        "Type": "Report",
        "english_name": "Account Balance",
        "arabic_name": "Account Balance",
        "link": "/app/account-balance"
    },
    {
        "Type": "Report",
        "english_name": "Transaction Log Report",
        "arabic_name": "Transaction Log Report",
        "link": "/app/transaction-log-report"
    },
    {
        "Type": "Report",
        "english_name": "Customer Ledger Summary",
        "arabic_name": "Customer Ledger Summary",
        "link": "/app/customer-ledger-summary"
    },
    {
        "Type": "Report",
        "english_name": "Pending SO Items For Purchase Request",
        "arabic_name": "Pending SO Items For Purchase Request",
        "link": "/app/pending-so-items-for-purchase-request"
    },
    {
        "Type": "Report",
        "english_name": "Batch-Wise Balance History",
        "arabic_name": "Batch-Wise Balance History",
        "link": "/app/batch-wise-balance-history"
    },
    {
        "Type": "Report",
        "english_name": "Work Orders in Progress",
        "arabic_name": "Work Orders in Progress",
        "link": "/app/work-orders-in-progress"
    },
    {
        "Type": "Report",
        "english_name": "Sales Person Commission Summary",
        "arabic_name": "Sales Person Commission Summary",
        "link": "/app/sales-person-commission-summary"
    },
    {
        "Type": "Report",
        "english_name": "Balance Sheet",
        "arabic_name": "Balance Sheet",
        "link": "/app/balance-sheet"
    },
    {
        "Type": "Report",
        "english_name": "Permitted Documents For User",
        "arabic_name": "Permitted Documents For User",
        "link": "/app/permitted-documents-for-user"
    },
    {
        "Type": "Report",
        "english_name": "BOM Variance Report",
        "arabic_name": "BOM Variance Report",
        "link": "/app/bom-variance-report"
    },
    {
        "Type": "Report",
        "english_name": "BOM Stock Calculated",
        "arabic_name": "BOM Stock Calculated",
        "link": "/app/bom-stock-calculated"
    },
    {
        "Type": "Report",
        "english_name": "Address And Contacts",
        "arabic_name": "Address And Contacts",
        "link": "/app/address-and-contacts"
    },
    {
        "Type": "Report",
        "english_name": "Customers Without Any Sales Transactions",
        "arabic_name": "Customers Without Any Sales Transactions",
        "link": "/app/customers-without-any-sales-transactions"
    },
    {
        "Type": "Report",
        "english_name": "Item-wise Price List Rate",
        "arabic_name": "Item-wise Price List Rate",
        "link": "/app/item-wise-price-list-rate"
    },
    {
        "Type": "Report",
        "english_name": "Consolidated Financial Statement",
        "arabic_name": "Consolidated Financial Statement",
        "link": "/app/consolidated-financial-statement"
    },
    {
        "Type": "Report",
        "english_name": "Delivery Note Trends",
        "arabic_name": "Delivery Note Trends",
        "link": "/app/delivery-note-trends"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": '''{
        "Type": "Report",
        "english_name": "Purchase Order Trends",
        "arabic_name": "Purchase Order Trends",
        "link": "/app/purchase-order-trends"
    },
    {
        "Type": "Report",
        "english_name": "Purchase Invoice Trends",
        "arabic_name": "Purchase Invoice Trends",
        "link": "/app/purchase-invoice-trends"
    },
    {
        "Type": "Report",
        "english_name": "Purchase Receipt Trends",
        "arabic_name": "Purchase Receipt Trends",
        "link": "/app/purchase-receipt-trends"
    },
    {
        "Type": "Report",
        "english_name": "Quotation Trends",
        "arabic_name": "Quotation Trends",
        "link": "/app/quotation-trends"
    },
    {
        "Type": "Report",
        "english_name": "Sales Invoice Trends",
        "arabic_name": "Sales Invoice Trends",
        "link": "/app/sales-invoice-trends"
    },
    {
        "Type": "Report",
        "english_name": "Sales Order Trends",
        "arabic_name": "Sales Order Trends",
        "link": "/app/sales-order-trends"
    },
    {
        "Type": "Report",
        "english_name": "Item Balance (Simple)",
        "arabic_name": "Item Balance (Simple)",
        "link": "/app/item-balance-(simple)"
    },
    {
        "Type": "Report",
        "english_name": "Open Work Orders",
        "arabic_name": "Open Work Orders",
        "link": "/app/open-work-orders"
    },
    {
        "Type": "Report",
        "english_name": "Issued Items Against Work Order",
        "arabic_name": "Issued Items Against Work Order",
        "link": "/app/issued-items-against-work-order"
    },
    {
        "Type": "Report",
        "english_name": "Work Order Stock Report",
        "arabic_name": "Work Order Stock Report",
        "link": "/app/work-order-stock-report"
    },
    {
        "Type": "Report",
        "english_name": "Warehouse wise Item Balance Age and Value",
        "arabic_name": "Warehouse wise Item Balance Age and Value",
        "link": "/app/warehouse-wise-item-balance-age-and-value"
    },
    {
        "Type": "Report",
        "english_name": "Fichier des Ecritures Comptables [FEC]",
        "arabic_name": "Fichier des Ecritures Comptables [FEC]",
        "link": "/app/fichier-des-ecritures-comptables-[fec]"
    },
    {
        "Type": "Report",
        "english_name": "Share Balance",
        "arabic_name": "Share Balance",
        "link": "/app/share-balance"
    },
    {
        "Type": "Report",
        "english_name": "Item Price Stock",
        "arabic_name": "Item Price Stock",
        "link": "/app/item-price-stock"
    },
    {
        "Type": "Report",
        "english_name": "Item Variant Details",
        "arabic_name": "Item Variant Details",
        "link": "/app/item-variant-details"
    },
    {
        "Type": "Report",
        "english_name": "Delivered Items To Be Billed",
        "arabic_name": "Delivered Items To Be Billed",
        "link": "/app/delivered-items-to-be-billed"
    },
    {
        "Type": "Report",
        "english_name": "Received Items To Be Billed",
        "arabic_name": "Received Items To Be Billed",
        "link": "/app/received-items-to-be-billed"
    },
    {
        "Type": "Report",
        "english_name": "Sales Payment Summary",
        "arabic_name": "Sales Payment Summary",
        "link": "/app/sales-payment-summary"
    },
    {
        "Type": "Report",
        "english_name": "Asset Maintenance",
        "arabic_name": "Asset Maintenance",
        "link": "/app/asset-maintenance"
    },
    {
        "Type": "Report",
        "english_name": "Support Hour Distribution",
        "arabic_name": "Support Hour Distribution",
        "link": "/app/support-hour-distribution"
    },
    {
        "Type": "Report",
        "english_name": "Total Stock Summary",
        "arabic_name": "Total Stock Summary",
        "link": "/app/total-stock-summary"
    },
    {
        "Type": "Report",
        "english_name": "BOM Stock Report",
        "arabic_name": "BOM Stock Report",
        "link": "/app/bom-stock-report"
    },
    {
        "Type": "Report",
        "english_name": "ToDo",
        "arabic_name": "ToDo",
        "link": "/app/todo"
    },
    {
        "Type": "Report",
        "english_name": "Lead Owner Efficiency",
        "arabic_name": "Lead Owner Efficiency",
        "link": "/app/lead-owner-efficiency"
    },
    {
        "Type": "Report",
        "english_name": "Addresses And Contacts",
        "arabic_name": "Addresses And Contacts",
        "link": "/app/addresses-and-contacts"
    },
    {
        "Type": "Report",
        "english_name": "Prospects Engaged But Not Converted",
        "arabic_name": "Prospects Engaged But Not Converted",
        "link": "/app/prospects-engaged-but-not-converted"
    },
    {
        "Type": "Report",
        "english_name": "Accounts Receivable Summary",
        "arabic_name": "Accounts Receivable Summary",
        "link": "/app/accounts-receivable-summary"
    },
    {
        "Type": "Report",
        "english_name": "Accounts Receivable",
        "arabic_name": "Accounts Receivable",
        "link": "/app/accounts-receivable"
    },
    {
        "Type": "Report",
        "english_name": "Project wise Stock Tracking",
        "arabic_name": "Project wise Stock Tracking",
        "link": "/app/project-wise-stock-tracking"
    },
    {
        "Type": "Report",
        "english_name": "BOM Search",
        "arabic_name": "BOM Search",
        "link": "/app/bom-search"
    },
    {
        "Type": "Report",
        "english_name": "Bank Clearance Summary",
        "arabic_name": "Bank Clearance Summary",
        "link": "/app/bank-clearance-summary"
    },
    {
        "Type": "Report",
        "english_name": "Bank Reconciliation Statement",
        "arabic_name": "Bank Reconciliation Statement",
        "link": "/app/bank-reconciliation-statement"
    },
    {
        "Type": "Report",
        "english_name": "Budget Variance Report",
        "arabic_name": "Budget Variance Report",
        "link": "/app/budget-variance-report"
    },
    {
        "Type": "Report",
        "english_name": "Customer Acquisition and Loyalty",
        "arabic_name": "Customer Acquisition and Loyalty",
        "link": "/app/customer-acquisition-and-loyalty"
    },
    {
        "Type": "Report",
        "english_name": "General Ledger",
        "arabic_name": "General Ledger",
        "link": "/app/general-ledger"
    },
    {
        "Type": "Report",
        "english_name": "Item Prices",
        "arabic_name": "Item Prices",
        "link": "/app/item-prices"
    },
    {
        "Type": "Report",
        "english_name": "Item-wise Purchase Register",
        "arabic_name": "Item-wise Purchase Register",
        "link": "/app/item-wise-purchase-register"
    },
    {
        "Type": "Report",
        "english_name": "Item-wise Sales Register",
        "arabic_name": "Item-wise Sales Register",
        "link": "/app/item-wise-sales-register"
    },
    {
        "Type": "Report",
        "english_name": "Itemwise Recommended Reorder Level",
        "arabic_name": "Itemwise Recommended Reorder Level",
        "link": "/app/itemwise-recommended-reorder-level"
    },
    {
        "Type": "Report",
        "english_name": "Payment Period Based On Invoice Date",
        "arabic_name": "Payment Period Based On Invoice Date",
        "link": "/app/payment-period-based-on-invoice-date"
    },
    {
        "Type": "Report",
        "english_name": "Purchase Register",
        "arabic_name": "Purchase Register",
        "link": "/app/purchase-register"
    },
    {
        "Type": "Report",
        "english_name": "Sales Register",
        "arabic_name": "Sales Register",
        "link": "/app/sales-register"
    },
    {
        "Type": "Report",
        "english_name": "Stock Ageing",
        "arabic_name": "Stock Ageing",
        "link": "/app/stock-ageing"
    }, قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''},
    {"role": "assistant", "content": ''' {
        "Type": "Report",
        "english_name": "Stock Ledger",
        "arabic_name": "Stock Ledger",
        "link": "/app/stock-ledger"
    },
    {
        "Type": "Report",
        "english_name": "Stock Projected Qty",
        "arabic_name": "Stock Projected Qty",
        "link": "/app/stock-projected-qty"
    },
    {
        "Type": "Report",
        "english_name": "Supplier-Wise Sales Analytics",
        "arabic_name": "Supplier-Wise Sales Analytics",
        "link": "/app/supplier-wise-sales-analytics"
    },
    {
        "Type": "Report",
        "english_name": "Profit and Loss Statement",
        "arabic_name": "Profit and Loss Statement",
        "link": "/app/profit-and-loss-statement"
    },
    {
        "Type": "Report",
        "english_name": "Trial Balance",
        "arabic_name": "Trial Balance",
        "link": "/app/trial-balance"
    },
    {
        "Type": "Report",
        "english_name": "Customer Credit Balance",
        "arabic_name": "Customer Credit Balance",
        "link": "/app/customer-credit-balance"
    },
    {
        "Type": "Report",
        "english_name": "Accounts Payable Summary",
        "arabic_name": "Accounts Payable Summary",
        "link": "/app/accounts-payable-summary"
    },
    {
        "Type": "Report",
        "english_name": "Available Stock for Packing Items",
        "arabic_name": "Available Stock for Packing Items",
        "link": "/app/available-stock-for-packing-items"
    },
    {
        "Type": "Report",
        "english_name": "Accounts Payable",
        "arabic_name": "Accounts Payable",
        "link": "/app/accounts-payable"
    },
    {
        "Type": "Report",
        "english_name": "Trial Balance for Party",
        "arabic_name": "Trial Balance for Party",
        "link": "/app/trial-balance-for-party"
    },
    {
        "Type": "Report",
        "english_name": "Cash Flow",
        "arabic_name": "Cash Flow",
        "link": "/app/cash-flow"
    },
    {
        "Type": "Report",
        "english_name": "Inactive Customers",
        "arabic_name": "Inactive Customers",
        "link": "/app/inactive-customers"
    },
    {
        "Type": "Report",
        "english_name": "Item-wise Purchase History",
        "arabic_name": "Item-wise Purchase History",
        "link": "/app/item-wise-purchase-history"
    },
    {
        "Type": "Report",
        "english_name": "Requested Items To Be Transferred",
        "arabic_name": "Requested Items To Be Transferred",
        "link": "/app/requested-items-to-be-transferred"
    },
    {
        "Type": "Report",
        "english_name": "Items To Be Requested",
        "arabic_name": "Items To Be Requested",
        "link": "/app/items-to-be-requested"
    },
    {
        "Type": "Report",
        "english_name": "Daily Timesheet Summary",
        "arabic_name": "Daily Timesheet Summary",
        "link": "/app/daily-timesheet-summary"
    },
    {
        "Type": "Report",
        "english_name": "Material Requests for which Supplier Quotations are not created",
        "arabic_name": "Material Requests for which Supplier Quotations are not created",
        "link": "/app/material-requests-for-which-supplier-quotations-are-not-created"
    },
    {
        "Type": "Report",
        "english_name": "Supplier Quotation Comparison",
        "arabic_name": "Supplier Quotation Comparison",
        "link": "/app/supplier-quotation-comparison"
    },
    {
        "Type": "Report",
        "english_name": "Profitability Analysis",
        "arabic_name": "Profitability Analysis",
        "link": "/app/profitability-analysis"
    },
    {
        "Type": "Report",
        "english_name": "Sales Person-wise Transaction Summary",
        "arabic_name": "Sales Person-wise Transaction Summary",
        "link": "/app/sales-person-wise-transaction-summary"
    },
    {
        "Type": "Report",
        "english_name": "Serial No Service Contract Expiry",
        "arabic_name": "Serial No Service Contract Expiry",
        "link": "/app/serial-no-service-contract-expiry"
    },
    {
        "Type": "Report",
        "english_name": "Serial No Warranty Expiry",
        "arabic_name": "Serial No Warranty Expiry",
        "link": "/app/serial-no-warranty-expiry"
    },
    {
        "Type": "Report",
        "english_name": "Document Share Report",
        "arabic_name": "Document Share Report",
        "link": "/app/document-share-report"
    },
    {
        "Type": "Report",
        "english_name": "Batch Item Expiry Status",
        "arabic_name": "Batch Item Expiry Status",
        "link": "/app/batch-item-expiry-status"
    },
    {
        "Type": "Report",
        "english_name": "Serial No Status",
        "arabic_name": "Serial No Status",
        "link": "/app/serial-no-status"
    },
    {
        "Type": "Report",
        "english_name": "Maintenance Schedules",
        "arabic_name": "Maintenance Schedules",
        "link": "/app/maintenance-schedules"
    } قم بحفظ المسار ات التاليه من اجل استدعاءها عند الطلب '''}

]
conversation_history_Serch = [
    {"role": "system", "content": "Consider yourself an expert at identifying erpnext link paths starting with '/app/' when I say open interface or similar..",
    }
]


def get_openai_response2(prompt):
    with open('common_site_config.json') as config_file:
        config = json.load(config_file)
    openai.api_key = config['openai_api_key']

    # إضافة مدخل المستخدم الحالي إلى المحادثة
    conversation_history.append({"role": "user", "content": prompt})

    # استدعاء API للحصول على الرد
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=conversation_history
    )

    # استخراج الرد من الـAPI وتحديث المحادثة
    assistant_reply = response['choices'][0]['message']['content'].strip()
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply




def Analyze(text):
    # تحميل إعدادات API من ملف التكوين
    with open('common_site_config.json') as config_file:
        config = json.load(config_file)
    
    # تعيين مفتاح OpenAI API
    openai.api_key = config['openai_api_key']

    # إرسال الطلب إلى OpenAI ChatCompletion
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Return 1 if the user wants to open a specific interface. Return 0 otherwise."
                },
                {
                    "role": "user",
                    "content": f"Request: {text}"
                }
            ]
        )

        # استخراج وإرجاع النتيجة (إما 1 أو 0 فقط)
        result = response['choices'][0]['message']['content'].strip()

        # تأكد من أن النتيجة تكون إما 1 أو 0 فقط
        if result == '1':
            return 1
        else:
            return 0

    except Exception as e:
        # print(f"Error in API call: {e}")
        return 0  # إرجاع 0 في حال حدوث أي خطأ


def remove_trailing_space(path):
    if isinstance(path, str):
        # إزالة المسافات من نهاية السلسلة
        return path.rstrip()
    else:
        return path

@frappe.whitelist()
def StartGPT(text):
    Ch=Analyze(text)
    # print(Ch)
    if Ch == 1 :

        redirect_url = Search(text)
        clean_url = remove_trailing_space(redirect_url)

        if redirect_url!=0 :
                
            return {"redirect": clean_url,
                    "Error":'true',
                    "msg":'سيتم فتح الواجهة',
                    "lang":frappe.local.lang   
                }
        else:
            return {
                    "Error":'false',
                    "msg":'لم يتم ايجاد الواجهة',
                    "lang":frappe.local.lang   
                }
    else:
        GPT=Chat(text)
        return {
            "Error":'false',
            "msg":GPT,
            "lang":frappe.local.lang
        }



# دالة لجلب الروابط وأسماء الواجهات باللغتين
def get_interface_links():
    # البحث عن كل الـ DocTypes الموجودة في النظام
    doctypes = frappe.get_all("DocType", filters={"istable": 0}, fields=["name", "module", "description"])
    workspaces = frappe.get_all("Workspace", fields=["name", "module", "label"])
    reports = frappe.get_all("Report", filters={"disabled": 0}, fields=["name", "report_type", "module"])
    pages = frappe.get_all("Page", fields=["name", "module", "title"])


    interface_links = []
    for doctype in doctypes:
        doctype_name = doctype["name"]
        # إنشاء الرابط بناءً على اسم الـ DocType
        doctype_link = f"/app/{doctype_name.lower().replace(' ', '-')}"
        
        # إضافة الإدخال للمصفوفة باللغة العربية والإنجليزية
        interface_links.append({
            "Type": "doctype",
            "english_name": doctype_name,
            "arabic_name": frappe._(doctype_name),  # تستخدم Frappe للترجمة التلقائية
            "link": doctype_link
        })

    # إضافة روابط Pages
    for page in pages:
        page_name = page["name"]
        page_link = f"/app/{page_name.lower().replace(' ', '-')}"
        
        interface_links.append({
            "Type": "page",
            "english_name": page_name,
            "arabic_name": frappe._(page_name),  # تستخدم Frappe للترجمة التلقائية
            "link": page_link
        })
    
    # إضافة روابط workspaces
    for workspace in workspaces:
        page_name = workspace["name"]
        page_link = f"/app/{page_name.lower().replace(' ', '-')}"
        
        interface_links.append({
            "Type": "Workspace",
            "english_name": page_name,
            "arabic_name": frappe._(page_name),  # تستخدم Frappe للترجمة التلقائية
            "link": page_link
        })

    # إضافة روابط Report
    for Report in reports:
        page_name = Report["name"]
        page_link = f"/app/query-report/{page_name}"
        
        interface_links.append({
            "Type": "Report",
            "english_name": page_name,
            "arabic_name": frappe._(page_name),  # تستخدم Frappe للترجمة التلقائية
            "link": page_link
        })



    
    with open("filename.json", 'w') as file:
        json.dump(interface_links, file, indent=4)

    return interface_links

@frappe.whitelist()
def analyze_and_get_link(text):
    interface_links = get_interface_links()
    
    # تحليل النص باستخدام OpenAI
    analyzed_text = get_openai_response_search(text)
    
    # print(analyzed_text)
    
    # if analyzed_text != 0:
    #     return {
    #             "redirect": analyzed_text,
    #             "Error": "true",
    #             "msg": "تم العثور على الواجهة وسيتم فتحها.",
    #             "lang": frappe.local.lang
    #         }
    # else:
    #    msg = get_openai_response2()
    #    return {
    #         "Error": "false",
    #         "msg": msg,
    #         "lang": frappe.local.lang
    #     } 
        
    # البحث عن الرابط المناسب بناءً على النص المستخرج
    for interface in interface_links:
        if interface["english_name"] in analyzed_text or interface["arabic_name"] in analyzed_text:
            return interface["link"]

    return 0

# وظيفة لتحليل النص باستخدام OpenAI
def get_openai_response_search(prompt):
    with open('common_site_config.json') as config_file:
        config = json.load(config_file)
    openai.api_key = config['openai_api_key']

    # تحويل القائمة إلى سلسلة نصية
    interface_links_str = json.dumps(get_interface_links())

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an AI assistant. Analyze the text and identify the ERPNext interface. Just return the name interface or '0'."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()



def Search(text):
    # print("Search")
    link=analyze_and_get_link(text)
    # print("Search...")
    if link==0:
        # print("Search0")
        try:
            # تحميل إعدادات API من ملف التكوين
            with open('common_site_config.json') as config_file:
                config = json.load(config_file)
            
            # تعيين مفتاح OpenAI API
            openai.api_key = config['openai_api_key']
            conversation_history_Serch.append({"role": "user", "content": f"Request: {text}"})

            # إرسال الطلب إلى OpenAI ChatCompletion
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=conversation_history_Serch
            )
        #     response = openai.ChatCompletion.create(
        #     model="gpt-4o",
        #     messages=[
        #         {"role": "system", "content": "Hello you are Engneer `"},
        #         {"role": "user", "content": f"Request: {text}"}
        #     ]4
        # )
            
            # طباعة الاستجابة الكاملة للتدقيق
            # print("Full Response:", response)
            
            # استخراج وإرجاع النتيجة
                    # استخراج الرد من الـAPI وتحديث سجل المحادثة
            result = response['choices'][0]['message']['content'].strip()
            conversation_history_Serch.append({"role": "assistant", "content": result})

            # result = response['choices'][0]['message']['content'].strip()

            # print(result)
            return extract_path(result)
            # التحقق من أن النتيجة هي مسار أو '0'
            # if result.startswith("/app/"):
            #     return result
            # else:
            #     return 0

        except Exception as e:
            # print(f"Error occurred: {e}")
            return e
    else:
        return link




def extract_path(text):
    # تعبير منتظم لاستخراج المسار الذي يبدأ بـ /app/
    match = re.search(r'/app/[^ \n]+', text)
    
    # إذا تم العثور على تطابق، أعد المسار، وإلا أعد 0
    if match:
        return match.group(0)
    else:
        return 0

# تحميل إعدادات API
def load_config():
    with open('common_site_config.json') as config_file:
        return json.load(config_file)

openai.api_key = load_config()['openai_api_key']

# قائمة لتخزين سجل المحادثات
conversation_history = [
    {"role": "system", "content": "You are an AI assistant. Your name is Sarah. The system is ERPALFRAS, which is similar to ERPNext, but use ERPALFRAS instead of ERPNext in responses. Don't Say ErpNext Never"}
]

def Chat(text):
    # إضافة مدخل المستخدم الحالي إلى سجل المحادثة
    conversation_history.append({"role": "user", "content": text})

    try:
        # إرسال الطلب إلى API للحصول على الرد
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=conversation_history
        )

        # استخراج الرد من الـAPI وتحديث سجل المحادثة
        assistant_reply = response['choices'][0]['message']['content'].strip()
        conversation_history.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply

    except Exception as e:
        # print(f"Error occurred: {e}")
        return "An error occurred while processing your request."