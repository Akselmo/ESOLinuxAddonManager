#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickStyle>
#include <iostream>
#include <AddonManager.h>
#include <AddonDownloader.h>

using namespace std;

int main(int argc, char* argv[])
{
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

    //TODO: Create objects for all the text fields
    //      Create objets/onclicks for buttons (?)
    //      Give these items to AddonManager class and do the rest in there
    QObject *rootObject = engine.rootObjects().first();
    QObject *qmlObject = rootObject->findChild<QObject*>("addonListTextArea");
    qmlObject->setProperty("text",QString("Hello"));

    return app.exec();
}
