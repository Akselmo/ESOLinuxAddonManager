//
// Created by akseli on 23/04/2022.
//

#ifndef _ADDONMANAGER_H_
#define _ADDONMANAGER_H_
#include <QGuiApplication>
#include <QDebug>
#include <QQmlContext>
#include <QQmlApplicationEngine>
#include <QQuickStyle>
#include <QQuickView>
#include <QFile>
#include <iostream>
#include <stdio.h>
using namespace std;


class AddonManager: public QObject
{
    Q_OBJECT
    //Default addon text files
    QString addonsLocationFile = "addonslocation.txt";
    QString addonsListFile = "addons.txt";

    //List the objects explicitly so it's easier to use them
    QObject *mainWindow;
    QObject *addonListTextArea;
    QObject *addonLocationTextField;
    QObject *addonListDownloadButton;
    QObject *radioButtonEU;
    QObject *radioButtonNA;
    QObject *ttcUpdateButton;

    //Addon files
    QString addonsLocation;
    QString addonsList;

    //Region
    QString selectedRegion = "EU";


public:
    AddonManager(QObject *rootObject, QQmlContext *rootContext);

    QString createOrReadFile(QString fileName);

    bool writeIntoFile(QString fileName, QByteArray data);

public slots:
    void downloadAddonsClicked();

    void downloadTtcClicked();

    void updateRegion(QString region);
};

#endif  //_ADDONMANAGER_H_
