# Apple School Manager and Apple Business APIs changelog

**Framework**: Apple School Manager and Apple Business APIs  
**Role**: Article

Learn about new features and updates in the Apple School Manager and Apple Business APIs.

### Overview

Use this changelog to learn about feature updates, deprecations, and removals for the Apple School Manager and Apple Business APIs.

### 2.7 (Apple Business) - 2026/10/29

### 1.8 (Apple School Manager) - 2026/10/29

New features for the Apple School Manager and Apple Business APIs

Added support for filtering devices by serial number, order number, product family, purchase source type, assignment status, date added to the organization, and order date:

- [Apple School Manager: Get Organization Devices.](../AppleSchoolManagerAPI/get-org-devices.md)
- [Apple Business: Get Organization Devices.](../AppleBusinessAPI/get-org-devices.md)

### 2.6 (Apple Business) - 2026/9/24

New features for the Apple Business APIs

Expanded the suite of identity services [Audit Events](../AppleBusinessAPI/get-audit-events.md) with the following event types.

- Account activity: `EXTERNAL_ACCOUNT_INVITED`, `ACCOUNT_PASSWORD_CHANGED`, `BATCH_PASSWORD_RESET_INITIATED`, `ACCOUNT_IMAGE_SET`, `ACCOUNT_IMAGE_REPLACED`, and `ACCOUNT_IMAGE_REMOVED`.
- Access management: `APPLE_SERVICES_SETTINGS_UPDATED`, `ROLE_CREATED`, and `ROLE_UPDATED`.
- Organization: `TERMS_ACCEPTED`, `IDP_CREATED`, `IDP_UPDATED`, `IDP_DELETED`, `IDP_ACCOUNT_SYNC_ENABLED`, `IDP_ACCOUNT_SYNC_DISABLED`, `DOMAIN_FEDERATION_ENABLED`, and `DOMAIN_FEDERATION_DISABLED`.

### 2.5 (Apple Business) - 2026/9/15

### 1.7 (Apple School Manager) - 2026/9/15

New features for the Apple School Manager and Apple Business APIs

Added support for retrieving a device’s Activation Lock status:

- [Apple School Manager: Get the Activation Lock Status for a Device.](../AppleSchoolManagerAPI/get-the-activation-lock-status-information-for-an-orgdevice.md)
- [Apple Business: Get the Activation Lock Status for a Device.](../AppleBusinessAPI/get-the-activation-lock-status-information-for-an-orgdevice.md)

### 2.4 (Apple Business) - 2026/8/26

New features for the Apple Business APIs

Added support for releasing devices using the following endpoint:

- [Assign, Unassign Devices to a Device Management Service or Release Devices.](../AppleBusinessAPI/create-an-orgdeviceactivity.md)

### 2.3 (Apple Business) - 2026/8/12

### 1.6 (Apple School Manager) - 2026/8/12

New features for the Apple School Manager and Apple Business APIs

Added support for device management service migration, allowing organizations to change device management services for their managed devices without erasing the device. Supports scheduling, updating, and canceling a device management service migration using the `orgDeviceActivities` activity types:

- [Apple School Manager: Assign or Unassign Devices to a Device Management Service.](../AppleSchoolManagerAPI/create-an-orgdeviceactivity.md)
- [Apple Business: Assign or Unassign Devices to a Device Management Service.](../AppleBusinessAPI/create-an-orgdeviceactivity.md)
- New read-only fields on organization devices: `isMdmMigrationCapable`, `mdmMigrationStatus`, and `mdmMigrationDeadlineDateTime`.

### 2.2 (Apple Business) - 2026/7/15

New features for the Apple Business APIs

Added support for organizational units using the following endpoints:

- [Get Organizational Units.](../AppleBusinessAPI/get-organizational-units.md)
- [Get Organizational Unit Information.](../AppleBusinessAPI/get-organizationalunit-information.md)
- [Get User IDs for an Organizational Unit.](../AppleBusinessAPI/get-all-user-ids-for-an-organizationalunit.md)

### 2.1 (Apple Business) - 2026/6/3

New features for the Apple Business APIs

Added support for managing device management services using the following endpoints:

- [Get Device Management Service Information.](../AppleBusinessAPI/get-mdmserver-information.md)
- [Create a Device Management Service.](../AppleBusinessAPI/create-an-mdmserver.md)
- [Update a Device Management Service.](../AppleBusinessAPI/update-an-mdmserver.md)
- [Delete a Device Management Service.](../AppleBusinessAPI/delete-an-mdmserver.md)

### 2.0 (Apple Business) - 2026/4/14

New features for the Apple Business APIs

Added the following endpoints:

- Audit events (to query organization audit events with filtering support)

  - [Retrieve a list of audit events for an organization.](../AppleBusinessAPI/get-audit-events.md)
- User and user group management services

  - [Get a list of users in an organization.](../AppleBusinessAPI/get-users.md)
  - [Get information about a specific user in an organization.](../AppleBusinessAPI/get-user-information.md)
  - [Get a list of user groups in an organization.](../AppleBusinessAPI/get-user-groups.md)
  - [Get information about a specific user group in an organization.](../AppleBusinessAPI/get-usergroup-information.md)
  - [Get a list of users assigned to a user group in an organization.](../AppleBusinessAPI/get-all-user-ids-for-a-user-group.md)
- Apps and packages

  - [Get the licensed apps in an organization.](../AppleBusinessAPI/get-apps.md)
  - [Get information about a specific app in an organization.](../AppleBusinessAPI/get-app-information.md)
  - [Get packages in an organization.](../AppleBusinessAPI/get-packages.md)
  - [Get information about a specific package in an organization.](../AppleBusinessAPI/get-package-information.md)

Added full Configuration management: create, read, update, delete, and support for custom Configurations

- [Get the list of Configurations in an organization.](../AppleBusinessAPI/get-configurations.md)
- [Get the details of a Configuration in an organization.](../AppleBusinessAPI/get-configuration-information.md)
- [Create a Configuration in an organization (of type CUSTOM_SETTING).](../AppleBusinessAPI/create-a-configuration.md)
- [Update a Configuration in an organization (of type CUSTOM_SETTING).](../AppleBusinessAPI/update-a-configuration.md)
- [Delete a Configuration in an organization.](../AppleBusinessAPI/delete-a-configuration.md)

Added full Blueprint management: create, read, update, delete, and endpoints to manage Blueprint relationships with apps, packages, configurations, devices, users, and user groups

- [Get a list of Blueprints in an organization.](../AppleBusinessAPI/get-blueprints.md)
- [Create a Blueprint in an organization.](../AppleBusinessAPI/create-a-blueprint.md)
- [Get information about a Blueprint in an organization.](../AppleBusinessAPI/get-blueprint-information.md)
- [Update a Blueprint in an organization.](../AppleBusinessAPI/update-a-blueprint.md)
- [Delete a Blueprint in an organization.](../AppleBusinessAPI/delete-a-blueprint.md)
- [Get a list of app IDs associated with a Blueprint.](../AppleBusinessAPI/get-all-app-ids-for-a-blueprint.md)
- [Add apps to a Blueprint.](../AppleBusinessAPI/add-apps-to-a-blueprint.md)
- [Remove apps from a Blueprint.](../AppleBusinessAPI/remove-apps-from-a-blueprint.md)
- [Get a list of Configuration IDs associated with a Blueprint.](../AppleBusinessAPI/get-all-configuration-ids-for-a-blueprint.md)
- [Add Configurations to a Blueprint.](../AppleBusinessAPI/add-configurations-to-a-blueprint.md)
- [Remove Configurations from a Blueprint.](../AppleBusinessAPI/remove-configurations-from-a-blueprint.md)
- [Get a list of package IDs associated with a Blueprint.](../AppleBusinessAPI/get-all-package-ids-for-a-blueprint.md)
- [Add packages to a Blueprint.](../AppleBusinessAPI/add-packages-to-a-blueprint.md)
- [Remove packages from a Blueprint.](../AppleBusinessAPI/remove-packages-from-a-blueprint.md)
- [Get a list of device IDs associated with a Blueprint.](../AppleBusinessAPI/get-all-orgdevice-ids-for-a-blueprint.md)
- [Add devices to a Blueprint.](../AppleBusinessAPI/add-org-devices-to-a-blueprint.md)
- [Remove devices from a Blueprint.](../AppleBusinessAPI/remove-org-devices-from-a-blueprint.md)
- [Get a list of user IDs associated with a Blueprint.](../AppleBusinessAPI/get-all-user-ids-for-a-blueprint.md)
- [Add users to a Blueprint.](../AppleBusinessAPI/add-users-to-a-blueprint.md)
- [Remove users from a Blueprint.](../AppleBusinessAPI/remove-users-from-a-blueprint.md)
- [Get a list of user group IDs associated with a Blueprint.](../AppleBusinessAPI/get-all-user-group-ids-for-a-blueprint.md)
- [Add user groups to a Blueprint.](../AppleBusinessAPI/add-user-groups-to-a-blueprint.md)
- [Remove user groups from a Blueprint.](../AppleBusinessAPI/remove-user-groups-from-a-blueprint.md)

Added support for retrieving devices enrolled in the built-in device management service

- [Get Devices Enrolled in the Apple Device Management Service.](../AppleBusinessAPI/get-apple-mdm-enrolled-devices.md)

Added detailed device information for devices enrolled in the built-in device management service

- [Get Details for a Device Enrolled in the Apple Device Management Service.](../AppleBusinessAPI/get-the-details-for-apple-mdm-enrolled-device.md)

### 1.5 (Apple School Manager and Apple Business) - 2026/1/20

Changes

- Updated Python script example to use PwJWT in the article Implementing OAuth for the Apple School and Business Manager API
- Updated MAC address types in Apple School Manager [OrgDevice.Attributes](../AppleSchoolManagerAPI/orgdevice/attributes-data.dictionary.md).
- Updated MAC address types in Apple Business [OrgDevice.Attributes](https://developer.apple.com/documentation/applebusinessmanagerapi/orgdevice/attributes-data.dictionary).

### 1.4 (Apple School Manager and Apple Business) - 2025/12/17

New features

- Added Wi-Fi, Bluetooth, and built-in Ethernet MAC address attributes for macOS to the [Apple School Manager API](../AppleSchoolManagerAPI/orgdevice/attributes-data.dictionary.md)
- Added Wi-Fi, Bluetooth, and built-in Ethernet MAC address attributes for macOS to the [Apple Business API](../AppleSchoolManagerAPI/orgdevice/attributes-data.dictionary.md)

### 1.3 (Apple School Manager and Apple Business) - 2025/11/5

New features

- Added AppleCare content to the Apple School Manager API
- Added AppleCare content to the [Apple Business API](https://developer.apple.com/documentation/applebusinessmanagerapi/get-all-apple-care-coverage-for-an-orgdevice)

### 1.2 (Apple School Manager and Apple Business) - 2025/07/16

New features

- Added Wi-Fi and Bluetooth MAC address attributes for iOS, iPadOS, tvOS, and visionOS to the [Apple School Manager API](../AppleSchoolManagerAPI/orgdevice/attributes-data.dictionary.md)
- Added Wi-Fi and Bluetooth MAC address attributes for iOS, iPadOS, tvOS, and visionOS to the [Apple Business API](../AppleSchoolManagerAPI/orgdevice/attributes-data.dictionary.md)

### 1.1 (Apple School Manager and Apple Business) - 2025/07/10

Changes

- Updated content in the article Implementing OAuth for the Apple School and Business Manager API


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-school-and-business-manager-api/apple-school-manager-and-apple-business-api-changelog)*