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

class AddonManager
{

public:
    QString createOrReadFile(QString fileName);
    void startUp();


};

#endif  //_ADDONMANAGER_H_
