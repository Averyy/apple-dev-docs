# Return a Personalized Pass

**Framework**: Wallet Passes  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create and sign a personalized pass, and send it to a device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Endpoint

`POST https://yourpasshost.example.com/v1/passes/{passTypeIdentifier}/{serialNumber}/personalize`

## Parameters

### Path Parameters

- `passTypeIdentifier` (string) *(required)*: The pass type identifier of the pass. This value corresponds to the value of the `passTypeIdentifier` key of the pass.
- `serialNumber` (string) *(required)*: The serial number of the pass. This value corresponds to the `serialNumber` key of the pass.

## Request Body

**Content-Type**: `application/json`  
**Type**: `PersonalizationDictionary`

An object that contains the personalization information for the pass.

## Responses

- `200` OK (`application/octet-stream`): The request is successful and returns a signed personalization token.

## See Also

### Personalized passes
- [object PersonalizationDictionary](./personalizationdictionary.md)
  An object that contains the information you use to personalize a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/return-a-personalized-pass)*