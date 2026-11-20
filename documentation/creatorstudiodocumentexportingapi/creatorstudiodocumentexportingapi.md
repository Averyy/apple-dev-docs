# Creator Studio Document Exporting API

**Framework**: Creator Studio Document Exporting API  
**Kind**: module  
**Role**: Framework

Convert documents to other formats, such as Portable Document Format (PDF), by using a web API.

**Availability**:
- Creator Studio 14.0+

## Overview

Use the Creator Studio API to convert documents from apps such as Numbers, Pages, and Keynote into other formats. With this API, your app can export a document to PDF and use the result to display an inline preview. Your app can also convert a Keynote Interchange Format file to a standard Keynote document.

The conversion service supports files that meet the following criteria:

- The file is no larger than 1 GB.
- Documents aren’t password protected.

> ❗ **Important**: As part of your uploading workflow, inform people that the service temporarily stores Creator Studio documents on Apple servers for the purpose of conversion. Provide the option to enable and disable the Creator Studio preview feature, and display a privacy notice such as “When using Creator Studio online previews, your files are temporarily stored on Apple servers.”

## Understand supported formats

The service can export a Creator Studio document to more than one format. Each format is identified by a uniform type identifier (UTI). Choose the format using the `export_format` parameter; for details, see [`Export a PDF document from a Creator Studio file`](./create-an-export-job-%28v2%29.md).

- **Portable Document Format (PDF)**: The Creator Studio API converts documents from Numbers, Pages, and Keynote to PDF. Use this format to display an inline preview for a Creator Studio document, or hand the document to the Preview app or another PDF-reader app. After the service exports a document to PDF, you can extract text and preview images from the PDF using standard tools. To export a document to PDF, use the UTI `com.adobe.pdf`.
- **Keynote Interchange Format**: To export a document to the Keynote Interchange Format, use the UTI `com.apple.keynote.interchange`. For an overview of the Keynote Interchange Format, see [Keynote Interchange Format](../keynoteinterchangeformat/keynoteinterchangeformat.md).

The service can also convert in the other direction: from a Keynote Interchange Format file to a standard Keynote document (`.key`). To convert a Keynote Interchange Format file, use a filename that ends in `.keyx` in the `encoded_filename` parameter, and use the UTI `com.apple.keynote.interchange`. The service detects the direction of the conversion from the filename extension, and returns a Keynote document. The service can’t convert a Keynote Interchange Format file to other formats, such as PDF.

## Sign up for the service

To use the Creator Studio document-exporting service, sign up by generating the keys and service identifier that the service requires. For more information about document exporting, see [Creator Studio Document Exporting](https://developer.apple.com/help/account/service-configurations/iwork-document-exporting/).

## Topics

### Endpoints
- [Export a PDF document from a Creator Studio file](./create-an-export-job-%28v2%29.md)
  Create a PDF preview of a Creator Studio document using JSON Web Token (JWT) authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/creatorstudiodocumentexportingapi)*