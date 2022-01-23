import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    id: window
    width: 500
    height: 500
    maximumHeight: height
    maximumWidth: width
    minimumHeight: height
    minimumWidth: width
    visible: true
    color: "#423d3d"
    title: qsTr("ESO Linux Addon Manager")

    Row {
        id: mainRow
        visible: true
        anchors.fill: parent
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.bottomMargin: 5
        anchors.topMargin: 5


        Row {
            id: addonLocationRow
            height: 65
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            layoutDirection: Qt.LeftToRight

            Label {
                id: addonLocationLabel
                text: qsTr("ESO Addon Location")
                anchors.top: parent.top
                anchors.topMargin: 10
                anchors.horizontalCenter: parent.horizontalCenter
                font.kerning: true
            }

            TextField {
                id: addonLocationTextField
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: addonLocationLabel.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10
                placeholderText: qsTr("/eso/addon/folder/location/")
            }

        }

        Row {
            id: addonListRow
            height: addonListScrollView.contentHeight + addonListDownloadButton.height
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: addonLocationRow.bottom
            anchors.topMargin: 10
            anchors.leftMargin: 10
            anchors.rightMargin: 10

            Label {
                id: addonListLabel
                text: qsTr("List of addons")
                anchors.top: parent.top
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 0
            }

            ScrollView {
                id: addonListScrollView
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: addonListLabel.bottom
                contentHeight: 250
                contentWidth: addonListRow.width
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10

                TextArea {
                    id: addonListTextArea
                    anchors.fill: parent
                    anchors.rightMargin: 10
                    anchors.bottomMargin: 10
                    placeholderText: qsTr("List addon link per row")
                }
            }

            Button {
                id: addonListDownloadButton
                text: qsTr("Download Addons")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: addonListScrollView.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10
            }

        }

        Row {
            id: ttcUpdaterRow
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: addonListRow.bottom
            anchors.bottom: parent.bottom
            anchors.topMargin: 50
            anchors.bottomMargin: 10
            anchors.rightMargin: 10
            anchors.leftMargin: 10

            Pane {
                id: ttcRegionPane
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.rightMargin: 0
                anchors.leftMargin: 0

                Label {
                    id: ttcRegionLabel
                    text: qsTr("Select TTC Region:")
                    horizontalAlignment: Text.AlignLeft

                    RadioButton {
                        id: radioButtonEU
                        text: qsTr("EU")
                        anchors.left: ttcRegionLabel.right
                        anchors.leftMargin: 5

                        RadioButton {
                            id: radioButtonNA
                            text: qsTr("NA")
                            anchors.horizontalCenterOffset: 60
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                    }
                }

            }

            Button {
                id: ttcUpdateButton
                text: qsTr("Update TTC Prices")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: ttcRegionPane.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10
            }


        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}D{i:8}D{i:7}D{i:5}D{i:14}D{i:11}D{i:10}
}
##^##*/
