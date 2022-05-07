#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickStyle>
#include <iostream>
#include <AddonManager.h>
#include <AddonDownloader.h>

using namespace std;


int main(int argc, char* argv[])
{
    //Initialize app
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif

    QGuiApplication app(argc, argv);

    QQuickStyle::setStyle("Plasma");
    QQuickStyle::setFallbackStyle("Fusion");
    // add fusion dark style colors here

    QQmlApplicationEngine engine;
    const QUrl url(QStringLiteral("qrc:/main.qml"));
    QObject::connect(
        &engine,
        &QQmlApplicationEngine::objectCreated,
        &app,
        [url](QObject* obj, const QUrl& objUrl)
        {
            if(!obj && url == objUrl)
                QCoreApplication::exit(-1);
        },
        Qt::QueuedConnection);
    engine.load(url);
    //End initialization

    //Create addonmanager
    QObject *rootObject = engine.rootObjects().first();
    AddonManager addonManager(rootObject);

    return app.exec();
}
