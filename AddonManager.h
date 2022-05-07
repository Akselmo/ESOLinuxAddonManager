//
// Created by akseli on 23/04/2022.
//

#ifndef _ADDONMANAGER_H_
#define _ADDONMANAGER_H_
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickStyle>
#include <QQuickView>
#include <QFile>
#include <iostream>
#include <stdio.h>
using namespace std;


class AddonManager
{
    //List the objects explicitly so it's easier to use them
    QObject *mainWindow;
    QObject *addonListTextArea;
    QObject *addonLocationTextField;
    QObject *addonListDownloadButton;
    QObject *radioButtonEU;
    QObject *radioButtonNA;
    QObject *ttcUpdateButton;

    //Addon files
    QString addons;
    QString addonsLocation;

public:
    AddonManager(QObject *rootObject);
    QString createOrReadFile(QString fileName);

};

#endif  //_ADDONMANAGER_H_
