# Home Assistant Custom Integration for Sony SDCP Projectors

## Overview
This custom integration for Home Assistant enables enhanced control over Sony SDCP projectors. It uses pySDCP just as the existing core integration does, but it's a significant improvement, offering a wider range of features and commands. Users can control their Sony projectors through Home Assistant, utilizing commands for power management, input selection, aspect ratio adjustment, and picture positioning.

## Features
- Power On/Off the projector
- Switch inputs (HDMI1, HDMI2)
- Adjust the aspect ratio (Normal, V Stretch, Zoom 1.85, Zoom 2.35, Stretch, Squeeze)
- Change the picture position (1.85, 2.35, Custom 1, Custom 2, Custom 3)

## Installation

### Via HACS (Home Assistant Community Store)
To install this custom integration via HACS, you'll first need to add it as a custom repository:

1. Open HACS in Home Assistant.
2. Navigate to 'Integrations'.
3. In the top right corner, click on the three dots and select 'Custom repositories'.
4. Enter the URL of this GitHub repository, choose 'Integration' in the 'Category' dropdown, and click 'Add'.
5. The Sony SDCP Projector Integration should now appear in the list of integrations available for installation in HACS.
6. Find and select "Sony SDCP Projector Integration", then click 'Install'.
7. Restart Home Assistant.

### Manual Installation
1. Download the integration from the GitHub repository.
2. Copy the `custom_components/sony_sdcp_projector` folder into the `config/custom_components` directory of your Home Assistant.
3. Restart Home Assistant.

## Configuration
Configure the integration through the Home Assistant UI:

1. Navigate to Configuration > Integrations.
2. Click "Add Integration".
3. Search for "Sony SDCP Projector" and follow the prompts to set it up.

## Usage
Control your Sony SDCP projector via the Home Assistant UI or automation scripts. 

### Service Calls
To send commands to the projector, use the `remote.send_command` service with the appropriate data. Example:

```yaml
service: remote.send_command
data:
  command: power_on
target:
  entity_id: remote.sony_sdcp_projector
```

Replace `power_on` with any of the following commands as needed:
- `power_off`
- `input_hdmi1`
- `input_hdmi2`
- `aspect_ratio_normal`
- `aspect_ratio_v_stretch`
- `aspect_ratio_zoom_1_85`
- `aspect_ratio_zoom_2_35`
- `aspect_ratio_stretch`
- `aspect_ratio_squeeze`
- `picture_position_1_85`
- `picture_position_2_35`
- `picture_position_custom_1`
- `picture_position_custom_2`
- `picture_position_custom_3`

## Support
For issues or queries, please file an issue on the GitHub repository.

## Contributing
Contributions are welcome. Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

*Note: This integration is not officially affiliated with or endorsed by Sony.*
