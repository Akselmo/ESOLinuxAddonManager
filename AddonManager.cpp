//
// Created by akseli on 23/04/2022.
//

#include "AddonManager.h"

QString createOrReadFile(QString fileName);

void startUp()
{
    QString addons = createOrReadFile("addons.txt");
    QString addonsLocation = createOrReadFile("addonslocation.txt");


}

QString createOrReadFile(QString fileName)
{
    QFile addonsFile(fileName);
    addonsFile.open(QIODevice::ReadWrite);
    return QString(addonsFile.readAll());
}
