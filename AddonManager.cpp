//
// Created by akseli on 23/04/2022.
//

#include "AddonManager.h"

AddonManager::AddonManager(QObject *rootObject, QQmlContext *rootContext) : QObject()
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
    addonsList = createOrReadFile(addonsListFile);
    addonsLocation = createOrReadFile(addonsLocationFile);

    //Add text from files to text fields
    addonListTextArea->setProperty("text", addonsList);
    addonLocationTextField->setProperty("text", addonsLocation);

    //Give the class for QML
    //HACK: Is this the proper way?
    rootContext->setContextProperty(QStringLiteral("_addonManager"), this);

}



QString AddonManager::createOrReadFile(QString fileName)
{
    QFile textFile(fileName);
    textFile.open(QIODevice::ReadWrite);
    return QString(textFile.readAll());
}

bool AddonManager::writeIntoFile(QString fileName, QByteArray data)
{
   bool success = false;
   QFile textFile(fileName);
   try
   {
       textFile.open(QIODevice::ReadWrite);
       textFile.write(data);
       success = true;
   }
   catch (exception e)
   {
       std::printf("%s \n", e.what());
   }
   return success;
}



//TODO: Check if theres better way to do this?
//For example just check if something is checked on runtime?
void AddonManager::updateRegion(QString region)
{
    selectedRegion = region;
}


// Button clicks
void AddonManager::downloadAddonsClicked()
{
    bool addonsListSuccess = writeIntoFile(addonsListFile, addonListTextArea->property("text").toByteArray());
    bool addonsLocationSuccess = writeIntoFile(addonsLocationFile, addonLocationTextField->property("text").toByteArray());

    qDebug() << "List saving success: " << addonsListSuccess;
    qDebug() << "Location saving success: " << addonsLocationSuccess;
}

void AddonManager::downloadTtcClicked()
{
    qDebug() << "TODO! Region enabled: " << selectedRegion;
}



