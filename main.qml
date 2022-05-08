import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: window
    objectName: "mainWindow"
    width: 500
    height: 500
    maximumHeight: height
    maximumWidth: width
    minimumHeight: height
    minimumWidth: width
    visible: true
    color: "#272727"
    //color: "#423d3d"
    title: qsTr("ESO Linux Addon Manager")

    Column {
        id: mainColumn
        visible: true
        anchors.fill: parent
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.bottomMargin: 5
        anchors.topMargin: 5


        Column {
            id: addonLocationColumn
            height: 65
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.rightMargin: 10
            anchors.leftMargin: 10

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
                objectName: "addonLocationTextField"
                text: none.none
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: addonLocationLabel.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10
                placeholderText: qsTr("/eso/addon/folder/location/")
            }

        }

        Column {
            id: addonListColumn
            height: addonListScrollView.contentHeight + addonListDownloadButton.height
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: addonLocationColumn.bottom
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
                contentWidth: addonListTextArea.width + 10
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10
                ScrollBar.vertical.visible: true

                TextArea {
                    id: addonListTextArea
                    objectName: "addonListTextArea"
                    text: none.none
                    anchors.fill: parent
                    wrapMode: Text.NoWrap
                    rightInset: 0
                    leftInset: 0
                    bottomInset: 0
                    topInset: 0
                    anchors.rightMargin: 10
                    anchors.bottomMargin: 10
                    placeholderText: qsTr("List addon link per row")
                }
            }

            Button {
                id: addonListDownloadButton
                objectName: "addonListDownloadButton"
                text: qsTr("Download Addons")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: addonListScrollView.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10

                Connections {
                    target: addonListDownloadButton
                    onClicked: _addonManager.downloadAddonsClicked();
                }
            }

        }

        Column {
            id: ttcUpdaterColumn
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: addonListColumn.bottom
            anchors.bottom: parent.bottom
            anchors.topMargin: 50
            anchors.bottomMargin: 10
            anchors.rightMargin: 10
            anchors.leftMargin: 10

            Pane {
                id: ttcRegionPane
                anchors.left: parent.left
                anchors.right: parent.right
                padding: 7
                contentHeight: 16
                contentWidth: 470
                anchors.rightMargin: 0
                anchors.leftMargin: 0

                Row {
                    id: row
                    anchors.fill: parent
                    spacing: 4

                    Label {
                        id: ttcRegionLabel
                        text: qsTr("Select TTC Region:")
                        horizontalAlignment: Text.AlignLeft
                        transformOrigin: Item.Center
                    }

                    RadioButton {
                        id: radioButtonEU
                        objectName: "radioButtonEU"
                        width: 50
                        text: qsTr("EU")
                        checked: true
                        onClicked: _addonManager.updateRegion("EU");
                    }

                    RadioButton {
                        id: radioButtonNA
                        objectName: "radioButtonNA"
                        text: qsTr("NA")
                        checked: false
                        onClicked: _addonManager.updateRegion("NA");
                    }
                }
            }

            Button {
                id: ttcUpdateButton
                objectName: "ttcUpdateButton"
                text: qsTr("Update TTC Prices")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: ttcRegionPane.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10

                Connections {
                    target: ttcUpdateButton
                    onClicked: _addonManager.downloadTtcClicked();
                }
            }


        }
    }
}








