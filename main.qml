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
                contentWidth: addonListColumn.width
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10

                TextArea {
                    id: addonListTextArea
                    anchors.fill: parent
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
                text: qsTr("Download Addons")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: addonListScrollView.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10
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
                        width: 50
                        text: qsTr("EU")
                        checked: true
                    }

                    RadioButton {
                        id: radioButtonNA
                        text: qsTr("NA")
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
    D{i:0;formeditorZoom:0.9}
}
##^##*/
