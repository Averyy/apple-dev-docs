# Recognizing tables within a document

**Framework**: Vision

Scan a document that contains a table and extract its content in a formatted way.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Xcode 26.0+

#### Overview

This sample app shows how to capture document images using the device camera and extract structured data from tables. The app uses the [`RecognizeDocumentsRequest`](recognizedocumentsrequest.md) API to detect a table and create a contact list from the extracted data.

When you run the app, you point your device camera at a document that contains a table of information. After capturing a photo, the app analyzes the table data and displays the formatted data so you can export the information to apps like Notes or Numbers.

The sample demonstrates three main capabilities:

1. Setting up camera capture with [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) to photograph documents.
2. Detecting a table in a document image using Vision.
3. Parsing structured data from table cells using DataDetection.

> **Note**: This sample code project is associated with WWDC25 session 272: [`Reading documents using Vision`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/272).

#### Configure the Sample Code Project

Because this sample app requires camera access, you’ll need to build and run this sample on a device. When you first launch the app on a device, grant the app access to the camera. In the sample project’s assets folder, open the `sampleDocuments.png` file and use the rear camera on iPad or iPhone to take a picture of the document. Optionally, if you have access to a printer, print this file and take a picture of it with your device.

#### Capture a Document Photo

The app starts by showing a camera preview where you can frame and take a picture of the document. To setup this preview and capture, the app creates a capture session with `AVFoundation`:

```swift
// Performs the initial capture session configuration.
private func setUpSession() throws {
    // Return early if already set up.
    guard !isSetUp else { return }

    // Retrieve the default camera.
    guard let defaultCamera = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: .back) else {
        throw CameraError.deviceUnavailable
    }

    // Add inputs for the default camera and microphone devices.
    activeVideoInput = try addInput(for: defaultCamera)

    // Configure the session preset based on the current capture mode.
    captureSession.sessionPreset = .photo
    // Add the photo capture output as the default output type.
    try addOutput(photoCapture.output)

    isSetUp = true
}
```

The `defaultCamera` uses the device’s rear camera and the `.photo` preset sets up the session to capture a picture of the document.

When you tap the capture button, the app calls `capturePhoto`:

```swift
func capturePhoto() async throws -> Data {
    try await photoCapture.capturePhoto()
}
```

This asynchronous method returns the captured photo as `Data`, which the app passes to the Vision model for analysis.

#### Detect Tables in the Document

The app uses Vision to find the table in the captured document image. To detect the table, the app uses [`RecognizeDocumentsRequest`](recognizedocumentsrequest.md). The Vision framework uses a default method for image processing: pass in the image, run the request, and get the extracted contents in an observation.

```swift
/// Process an image and return the first table detected.
private func extractTable(from image: Data) async throws -> DocumentObservation.Container.Table {

    // The Vision request.
    let request = RecognizeDocumentsRequest()

    // Perform the request on the image data and return the results.
    let observations = try await request.perform(on: image)

    // Get the first observation from the array.
    guard let document = observations.first?.document else {
        throw AppError.noDocument
    }

    // Extract the first table detected.
    guard let table = document.tables.first else {
        throw AppError.noTable
    }

    return table
}
```

The `request.perform(on:)` method runs the [`RecognizeDocumentsRequest`](recognizedocumentsrequest.md) on the image and returns a [`DocumentObservation`](documentobservation.md). Each document is a container that holds text, tables, lists, or barcodes. The app accesses the table from the document’s [`DocumentObservation.Container.Table`](documentobservation/container/table.md) property.

The app highlights the detected table with a blue outline showing the boundaries.

#### Extract Contact Information From Table Cells

With the extracted structure, the app can access the data in the table cells. The app parses through the rows and columns to get the table data and converts it to an array of `Contact` objects:

```swift
/// Extract the name, email address, and phone number from a table into a list of contacts.
private func parseTable(_ table: DocumentObservation.Container.Table) -> [Contact] {
    var contacts = [Contact]()

    // Iterate over each row in the table.
    for row in table.rows {
        // Take the contact name from the first column.
        guard let firstCell = row.first else {
            continue
        }
        // Extract the text content from the transcript.
        let name = firstCell.content.text.transcript

        // Look for email addresses and phone numbers in the remaining cells.
        var detectedPhone: String? = nil
        var detectedEmail: String? = nil

        for cell in row.dropFirst() {
            // Get all detected data in the cell, then match emails and phone numbers to a contact. 
            for data in cell.content.text.detectedData {
                switch data.match.details {
                case .emailAddress(let email):
                    detectedEmail = email.emailAddress
                case .phoneNumber(let phoneNumber):
                    detectedPhone = phoneNumber.phoneNumber
                default:
                    break
                }
            }
        }

        // Create a contact if an email was detected.
        if let email = detectedEmail {
            let contact = Contact(name: name, email: email, phoneNumber: detectedPhone)
            contacts.append(contact)
        }
    }

    return contacts
}
```

The app takes the contact name from the first column and accesses the text content using the  [`transcript`](DocumentObservation/Container/Text-swift.struct/transcript.md) property.

To process the remaining columns, the app skips the first cell by using [`dropFirst(_:)`](https://developer.apple.com/documentation/Swift/Array/dropFirst(_:)) on the row. It uses the [`DataDetection`](https://developer.apple.com/documentation/DataDetection) framework to find email addresses and phone numbers in the `cell.content.text.detectedData` array.

The app creates a contact only when it finds an email address. After processing the table, the app stores all the contacts in an array and people can view it through the `ContactView`.

```swift
struct ContactView: View {
    let contacts: [Contact]
    var body: some View {
        Text("Contacts")
        List(contacts, id: \.name) { contact in
            HStack {
                Text(contact.name)
                Spacer()
                Text(contact.email)
                Spacer()
                Text(contact.phoneNumber ?? "")
            }
        }
    }
}
```

A person can see this list of extracted contacts in the app by clicking the View Contacts button above the photo capture. Each entry shows the contact’s name and email address, with phone numbers included when detected in the table.

#### Interact with Table Cells

The app allows you to tap on the cells in the captured table and use the data within the cells to call or send a message. It uses the [`boundingRegion`](DocumentObservation/Container/Table/boundingRegion.md) property of the `DocumentObservation` to access the selected cell and to ensure that people only tap within the table bounds.

```swift
extension DocumentObservation.Container.Table {
    /// Returns the contents of a cell that someone taps.
    func cell(at point: NormalizedPoint) -> TableCell? {
        let visionPoint = point.cgPoint
        // Verify that the tap occurs inside the bounding region of the table.
        guard self.boundingRegion.normalizedPath.contains(visionPoint) else {
            return nil
        }
        // Inspect each cell.
        for row in self.rows {
            for cell in row {
                // Check if the tap occurs inside the cell.
                if cell.content.boundingRegion.normalizedPath.contains(visionPoint) {
                    return TableCell(cell)
                }
            }
        }
        return nil
    }
}
```

The method first verifies that the tap occurs within the table’s overall `boundingRegion`, then iterates through each cell’s `boundingRegion` to find the one that contains the tap. Bounding regions use normalized coordinates (`0.0` to `1.0`) relative to the image dimensions, which makes them work at any display scale.

When the method finds a cell, the app displays a popup showing the cell’s content. If the cell contains an email address, people can tap on the address to compose a message. For phone numbers, people can tap to call or send a text message.

#### Export Table Data

You can also export the table data in tab-separated values (TSV) format to copy and paste into compatible apps like Notes or Numbers:

```swift
/// Convert the table into a TSV string format that's compatible with pasting into Notes or Numbers.
///
/// Tables have at most one line per cell, and no cells that span multiple rows or columns.
func exportTable() async throws -> String {
    guard let rows = self.table?.rows else {
        throw AppError.noTable
    }
    // Map each row into a tab-delimited line.
    let tableRowData = rows.map { row in
        return row.map({ $0.content.text.transcript }).joined(separator: "\t")
    }
    // Create a multiline string with one row per line.
    return tableRowData.joined(separator: "\n")
}
```

Each row becomes a line in the output string, with the `transcript` property providing the recognized text from each cell. The `"\t"` separator creates the TSV format by placing tab characters between cells in the same row. The outer `joined(separator: "\n")` call puts each row on its own line.

People can tap the `Copy Table` button to copy this formatted text to the clipboard, then paste it into other apps. The table structure remains intact when pasted.

## See Also

- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [struct DetectBarcodesRequest](detectbarcodesrequest.md)
  A request that detects barcodes in an image.
- [struct DetectDocumentSegmentationRequest](detectdocumentsegmentationrequest.md)
  A request that detects rectangular regions that contain text in the input image.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [struct RecognizeDocumentsRequest](recognizedocumentsrequest.md)
  An image-analysis request to scan an image of a document and provide information about its structure.
- [struct RecognizeTextRequest](recognizetextrequest.md)
  An image-analysis request that recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognize-tables-within-a-document)*