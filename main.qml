import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    id: window
    width: 500
    height: 500
    visible: true
    color: "#393636"
    title: qsTr("Hello World")
    palette.highlight: "gold"

    Row {
        id: main_row
        visible: true
        anchors.fill: parent
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.bottomMargin: 5
        anchors.topMargin: 5

        Row {
            id: addon_location
            width: window.width
            height: 50
            anchors.horizontalCenter: parent.horizontalCenter
            layoutDirection: Qt.LeftToRight

            Text {
                id: addon_location_description
                width: window.width - 20
                height: 30
                color: "#ffffff"
                text: "ESO Addon folder location"
                anchors.top: parent.top
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.NoWrap
                font.family: window.font.family
                styleColor: "#ffffff"
                anchors.topMargin: 5
                anchors.horizontalCenter: parent.horizontalCenter
            }

            TextField {
                id: addon_location_field
                width: window.width - 20
                height: 30
                color: "#ffffff"
                text: "/game/addon/location/here"
                anchors.top: addon_location_description.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignTop
                bottomPadding: 5
                topPadding: 5
                font.family: window.font.family
                rightPadding: 5
                leftPadding: 5
                selectedTextColor: "#000000"
                selectionColor: "#9d9dff"
                anchors.topMargin: 0
                anchors.horizontalCenter: parent.horizontalCenter
            }

        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}
}
##^##*/
