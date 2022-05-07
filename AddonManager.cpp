//
// Created by akseli on 23/04/2022.
//

#include "AddonManager.h"

AddonManager::AddonManager(QObject *rootObject)
{
    //Initialize usable elements
    mainWindow = rootObject->findChild<QObject*>("mainWindow");
    addonListTextArea = rootObject->findChild<QObject*>("addonListTextArea");
    addonLocationTextField = rootObject->findChild<QObject*>("addonLocationTextField");
    addonListDownloadButton = rootObject->findChild<QObject*>("addonListDownloadButton");
    radioButtonEU = rootObject->findChild<QObject*>("radioButtonEU");
    radioButtonNA = rootObject->findChild<QObject*>("radioButtonNA");
    ttcUpdateButton = rootObject->findChild<QObject*>("ttcUpdateButton");

    //Initialize addon files
    addons = createOrReadFile("addons.txt");
    addonsLocation = createOrReadFile("addonslocation.txt");

    //Add text from files to text fields
    addonListTextArea->setProperty("text", addons);
    addonLocationTextField->setProperty("text", addonsLocation);

}



QString AddonManager::createOrReadFile(QString fileName)
{
    QFile addonsFile(fileName);
    addonsFile.open(QIODevice::ReadWrite);
    return QString(addonsFile.readAll());
}


