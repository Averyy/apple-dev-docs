# iWork Document Exporting API

**Framework**: iWork Document Exporting API  
**Kind**: module

Convert iWork documents to Portable Document Format (PDF) files using a web API.

**Availability**:
- iWork 14.0+

#### Overview

The iWork API enables the conversion of iWork documents from apps such as Numbers, Pages, and Keynote into PDF documents that a person can view using the Preview app or another PDF reader application.

Once the service exports an iWork document to PDF format, an app can use the PDF to display an inline preview for iWork documents. You can extract Text and preview images from the PDF document using standard tools.

The conversion service supports files that meet the following criteria:

- A maximum file size of 1 GB.
- Documents that aren’t protected with a password.

> ❗ **Important**: As part of your uploading workflow, inform people that the service temporarily stores iWork documents on Apple servers for the purpose of conversion. Provide the option to enable and disable the iWork preview feature, and display a privacy notice such as “When using iWork online previews, your files will be temporarily stored on Apple servers.”

As part of your uploading workflow, inform people that the service temporarily stores iWork documents on Apple servers for the purpose of conversion. Provide the option to enable and disable the iWork preview feature, and display a privacy notice such as “When using iWork online previews, your files will be temporarily stored on Apple servers.”

To convert iWork documents to PDF files using the iWork document-exporting service, sign up by generating the keys and service identifier the service requires. This process consists of several steps that you need to perform in the order described below.

##### Log in to the Developer Portal

Log into the developer portal by accessing [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com) using your Apple Developer ID. After logging in, click on the Identifiers item in the Certificates, IDs & Profiles section.

Make note of your developer team ID, located under your account name in the upper-right corner of the window; the service requires this value when making calls to the service API.

##### Create a New Identifier

To create a new identifier, perform these steps:

1. Click the + button to create a new identifier.
2. On the Register a new identifier page, click Services IDs, and then click Continue.
3. Enter a description for the new service ID and a unique identifier. Use a reverse domain style sting, such as `com.example.myAppName`, and click Continue.
4. Click Register to save your new service ID; the developer portal then displays a list of available identifiers.
5. Click on the newly created identifier.
6. Enable iWork Document Export, click Continue, and then click Save.

##### Create and Download a New Key

To create a new key, perform these steps:

1. Click Keys in the sidebar.
2. Provide a unique name for the new key.
3. Select iWork Document Exporting from the list of key types.
4. Click Continue to configure the new key.
5. From the dropdown menu, select the name of the identifier you created earlier.
6. Click Save to bind the service name to the key.
7. Click Download to save the new key. This key can’t be downloaded again; if it’s lost or compromised, you’ll need to revoke it and generate a new key. Keep copies of the key in a safe place.

## Topics

### Endpoints
- [Export a PDF document from an iWork file](create-an-export-job-(v2).md)
  Create a PDF preview of an iWork document using JSON Web Token (JWT) authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iWorkDocumentExportingAPI)*