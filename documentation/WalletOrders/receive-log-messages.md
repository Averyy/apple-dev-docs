# Receive log messages

**Framework**: Wallet Orders  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Records log messages on your server.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Endpoint

`POST https://your-web-service.com/v1/log`

## Request Body

**Content-Type**: `application/json`  
**Type**: `LogEntries`

An array of log messages.

## Responses

- `200` OK: The request was successful.

## See Also

### Message logs
- [object LogEntries](./logentries.md)
  An array of log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/receive-log-messages)*