
#ifndef FORMXDDIAM_H
#define FORMXDDIAM_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QOpenGLWidget>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSlider>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *full_window_widget;
    QHBoxLayout *horizontalLayout;
    QFrame *side_frame;
    QVBoxLayout *verticalLayout;
    QFrame *side_frame_header;
    QHBoxLayout *horizontalLayout_6;
    QFrame *header_content;
    QHBoxLayout *horizontalLayout_12;
    QPushButton *pushButton;
    QFrame *side_frame_content;
    QHBoxLayout *horizontalLayout_3;
    QFrame *side_frame_contents;
    QVBoxLayout *verticalLayout_2;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents_2;
    QVBoxLayout *verticalLayout_8;
    QFrame *frame;
    QFrame *frame_2;
    QFrame *frame_9;
    QFrame *frame_10;
    QFrame *side_frame_bottom;
    QHBoxLayout *horizontalLayout_2;
    QFrame *file_operations;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *open_file_button;
    QPushButton *save_file_button;
    QFrame *folder_operations;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *open_folder_button;
    QPushButton *select_folder_button;
    QFrame *main_frame;
    QVBoxLayout *verticalLayout_3;
    QFrame *main_frame_header;
    QHBoxLayout *horizontalLayout_7;
    QFrame *frame_7;
    QHBoxLayout *horizontalLayout_9;
    QPushButton *side_frame_call_button;
    QFrame *search_frame;
    QHBoxLayout *horizontalLayout_10;
    QLineEdit *searck_input;
    QPushButton *download_button;
    QPushButton *login_button;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_8;
    QPushButton *roll_down_button;
    QPushButton *expand_button;
    QPushButton *close_button;
    QFrame *main_frame_content;
    QHBoxLayout *horizontalLayout_11;
    QOpenGLWidget *openGLWidget;
    QFrame *main_frame_bottom;
    QVBoxLayout *verticalLayout_4;
    QFrame *tools_frame;
    QVBoxLayout *verticalLayout_9;
    QFrame *frame_3;
    QVBoxLayout *verticalLayout_10;
    QSlider *horizontalSlider;
    QScrollArea *scrollArea_2;
    QWidget *scrollAreaWidgetContents_3;
    QVBoxLayout *verticalLayout_11;
    QFrame *frame_8;
    QFrame *frame_4;
    QFrame *frame_6;
    QFrame *info_frame;
    QHBoxLayout *horizontalLayout_13;
    QFrame *video_name_frame;
    QVBoxLayout *verticalLayout_5;
    QLabel *video_name;
    QFrame *status_frame;
    QVBoxLayout *verticalLayout_6;
    QLabel *status;
    QFrame *progress_bar_frame;
    QVBoxLayout *verticalLayout_7;
    QProgressBar *progressBar;
    QFrame *corner_holder;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->setWindowModality(Qt::NonModal);
        MainWindow->resize(1093, 682);
        QFont font;
        font.setFamily(QStringLiteral("Roboto"));
        MainWindow->setFont(font);
        MainWindow->setStyleSheet(QLatin1String("*{\n"
"border:none;\n"
"}\n"
""));
        MainWindow->setIconSize(QSize(25, 25));
        MainWindow->setTabShape(QTabWidget::Rounded);
        full_window_widget = new QWidget(MainWindow);
        full_window_widget->setObjectName(QStringLiteral("full_window_widget"));
        full_window_widget->setStyleSheet(QStringLiteral("background-color:rgb(24,24,36);"));
        horizontalLayout = new QHBoxLayout(full_window_widget);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        side_frame = new QFrame(full_window_widget);
        side_frame->setObjectName(QStringLiteral("side_frame"));
        side_frame->setMinimumSize(QSize(250, 0));
        side_frame->setMaximumSize(QSize(250, 16777215));
        side_frame->setStyleSheet(QStringLiteral("background-color: rgb(0, 4, 31)"));
        side_frame->setFrameShape(QFrame::StyledPanel);
        side_frame->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(side_frame);
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        side_frame_header = new QFrame(side_frame);
        side_frame_header->setObjectName(QStringLiteral("side_frame_header"));
        side_frame_header->setMaximumSize(QSize(16777215, 50));
        side_frame_header->setFrameShape(QFrame::StyledPanel);
        side_frame_header->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(side_frame_header);
        horizontalLayout_6->setSpacing(0);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        horizontalLayout_6->setContentsMargins(0, 0, 0, 0);
        header_content = new QFrame(side_frame_header);
        header_content->setObjectName(QStringLiteral("header_content"));
        header_content->setStyleSheet(QStringLiteral("background-color: rgb(0, 4, 31)"));
        header_content->setFrameShape(QFrame::StyledPanel);
        header_content->setFrameShadow(QFrame::Raised);
        horizontalLayout_12 = new QHBoxLayout(header_content);
        horizontalLayout_12->setSpacing(0);
        horizontalLayout_12->setObjectName(QStringLiteral("horizontalLayout_12"));
        horizontalLayout_12->setContentsMargins(0, 4, 0, 0);
        pushButton = new QPushButton(header_content);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        QIcon icon;
        icon.addFile(QStringLiteral("../resources/Icons/header.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon);
        pushButton->setIconSize(QSize(160, 52));

        horizontalLayout_12->addWidget(pushButton);


        horizontalLayout_6->addWidget(header_content);


        verticalLayout->addWidget(side_frame_header);

        side_frame_content = new QFrame(side_frame);
        side_frame_content->setObjectName(QStringLiteral("side_frame_content"));
        side_frame_content->setFrameShape(QFrame::StyledPanel);
        side_frame_content->setFrameShadow(QFrame::Raised);
        horizontalLayout_3 = new QHBoxLayout(side_frame_content);
        horizontalLayout_3->setSpacing(0);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(5, 0, 0, 0);
        side_frame_contents = new QFrame(side_frame_content);
        side_frame_contents->setObjectName(QStringLiteral("side_frame_contents"));
        side_frame_contents->setFrameShape(QFrame::StyledPanel);
        side_frame_contents->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(side_frame_contents);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        scrollArea = new QScrollArea(side_frame_contents);
        scrollArea->setObjectName(QStringLiteral("scrollArea"));
        scrollArea->setLayoutDirection(Qt::RightToLeft);
        scrollArea->setStyleSheet(QStringLiteral(""));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QStringLiteral("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 231, 650));
        verticalLayout_8 = new QVBoxLayout(scrollAreaWidgetContents_2);
        verticalLayout_8->setSpacing(10);
        verticalLayout_8->setObjectName(QStringLiteral("verticalLayout_8"));
        verticalLayout_8->setContentsMargins(10, 10, 10, 10);
        frame = new QFrame(scrollAreaWidgetContents_2);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setMinimumSize(QSize(0, 150));
        frame->setMaximumSize(QSize(16777215, 150));
        frame->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,100);"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);

        verticalLayout_8->addWidget(frame);

        frame_2 = new QFrame(scrollAreaWidgetContents_2);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setMinimumSize(QSize(0, 150));
        frame_2->setSizeIncrement(QSize(0, 150));
        frame_2->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,100);"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);

        verticalLayout_8->addWidget(frame_2);

        frame_9 = new QFrame(scrollAreaWidgetContents_2);
        frame_9->setObjectName(QStringLiteral("frame_9"));
        frame_9->setMinimumSize(QSize(0, 150));
        frame_9->setMaximumSize(QSize(16777215, 150));
        frame_9->setSizeIncrement(QSize(0, 0));
        frame_9->setBaseSize(QSize(0, 0));
        frame_9->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,100);"));
        frame_9->setFrameShape(QFrame::StyledPanel);
        frame_9->setFrameShadow(QFrame::Raised);

        verticalLayout_8->addWidget(frame_9);

        frame_10 = new QFrame(scrollAreaWidgetContents_2);
        frame_10->setObjectName(QStringLiteral("frame_10"));
        frame_10->setMinimumSize(QSize(0, 150));
        frame_10->setMaximumSize(QSize(16777215, 150));
        frame_10->setSizeIncrement(QSize(0, 0));
        frame_10->setBaseSize(QSize(0, 0));
        frame_10->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,100);"));
        frame_10->setFrameShape(QFrame::StyledPanel);
        frame_10->setFrameShadow(QFrame::Raised);

        verticalLayout_8->addWidget(frame_10);

        scrollArea->setWidget(scrollAreaWidgetContents_2);

        verticalLayout_2->addWidget(scrollArea);


        horizontalLayout_3->addWidget(side_frame_contents);


        verticalLayout->addWidget(side_frame_content);

        side_frame_bottom = new QFrame(side_frame);
        side_frame_bottom->setObjectName(QStringLiteral("side_frame_bottom"));
        side_frame_bottom->setMaximumSize(QSize(16777215, 50));
        side_frame_bottom->setStyleSheet(QStringLiteral("background-color: rgb(0, 4, 31)"));
        side_frame_bottom->setFrameShape(QFrame::StyledPanel);
        side_frame_bottom->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(side_frame_bottom);
        horizontalLayout_2->setSpacing(0);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        file_operations = new QFrame(side_frame_bottom);
        file_operations->setObjectName(QStringLiteral("file_operations"));
        file_operations->setFrameShape(QFrame::StyledPanel);
        file_operations->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(file_operations);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        open_file_button = new QPushButton(file_operations);
        open_file_button->setObjectName(QStringLiteral("open_file_button"));
        open_file_button->setEnabled(true);
        open_file_button->setMinimumSize(QSize(30, 30));
        open_file_button->setMaximumSize(QSize(30, 30));
        QIcon icon1;
        icon1.addFile(QStringLiteral("../resources/Icons/open_file.svg"), QSize(), QIcon::Normal, QIcon::Off);
        open_file_button->setIcon(icon1);
        open_file_button->setIconSize(QSize(25, 25));
        open_file_button->setAutoDefault(false);
        open_file_button->setFlat(true);

        horizontalLayout_4->addWidget(open_file_button);

        save_file_button = new QPushButton(file_operations);
        save_file_button->setObjectName(QStringLiteral("save_file_button"));
        save_file_button->setMinimumSize(QSize(30, 30));
        save_file_button->setMaximumSize(QSize(30, 30));
        QIcon icon2;
        icon2.addFile(QStringLiteral("../resources/Icons/save_file.svg"), QSize(), QIcon::Normal, QIcon::Off);
        save_file_button->setIcon(icon2);
        save_file_button->setIconSize(QSize(25, 25));

        horizontalLayout_4->addWidget(save_file_button);


        horizontalLayout_2->addWidget(file_operations);

        folder_operations = new QFrame(side_frame_bottom);
        folder_operations->setObjectName(QStringLiteral("folder_operations"));
        folder_operations->setFrameShape(QFrame::StyledPanel);
        folder_operations->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(folder_operations);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        open_folder_button = new QPushButton(folder_operations);
        open_folder_button->setObjectName(QStringLiteral("open_folder_button"));
        open_folder_button->setMinimumSize(QSize(30, 30));
        open_folder_button->setMaximumSize(QSize(30, 30));
        QIcon icon3;
        icon3.addFile(QStringLiteral("../resources/Icons/open_folder.svg"), QSize(), QIcon::Normal, QIcon::Off);
        open_folder_button->setIcon(icon3);
        open_folder_button->setIconSize(QSize(38, 25));

        horizontalLayout_5->addWidget(open_folder_button);

        select_folder_button = new QPushButton(folder_operations);
        select_folder_button->setObjectName(QStringLiteral("select_folder_button"));
        select_folder_button->setMinimumSize(QSize(30, 30));
        select_folder_button->setMaximumSize(QSize(30, 30));
        QIcon icon4;
        icon4.addFile(QStringLiteral("../resources/Icons/select_folder.svg"), QSize(), QIcon::Normal, QIcon::Off);
        select_folder_button->setIcon(icon4);
        select_folder_button->setIconSize(QSize(25, 25));

        horizontalLayout_5->addWidget(select_folder_button);


        horizontalLayout_2->addWidget(folder_operations);


        verticalLayout->addWidget(side_frame_bottom);


        horizontalLayout->addWidget(side_frame);

        main_frame = new QFrame(full_window_widget);
        main_frame->setObjectName(QStringLiteral("main_frame"));
        main_frame->setFrameShape(QFrame::StyledPanel);
        main_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(main_frame);
        verticalLayout_3->setSpacing(0);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        main_frame_header = new QFrame(main_frame);
        main_frame_header->setObjectName(QStringLiteral("main_frame_header"));
        main_frame_header->setMinimumSize(QSize(0, 50));
        main_frame_header->setMaximumSize(QSize(16777215, 50));
        main_frame_header->setStyleSheet(QStringLiteral("background-color: rgb(0, 4, 31)"));
        main_frame_header->setFrameShape(QFrame::StyledPanel);
        main_frame_header->setFrameShadow(QFrame::Raised);
        horizontalLayout_7 = new QHBoxLayout(main_frame_header);
        horizontalLayout_7->setSpacing(0);
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));
        horizontalLayout_7->setContentsMargins(0, 0, 0, 0);
        frame_7 = new QFrame(main_frame_header);
        frame_7->setObjectName(QStringLiteral("frame_7"));
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        horizontalLayout_9 = new QHBoxLayout(frame_7);
        horizontalLayout_9->setObjectName(QStringLiteral("horizontalLayout_9"));
        side_frame_call_button = new QPushButton(frame_7);
        side_frame_call_button->setObjectName(QStringLiteral("side_frame_call_button"));
        QIcon icon5;
        icon5.addFile(QStringLiteral("../resources/Icons/side_menu.svg"), QSize(), QIcon::Normal, QIcon::Off);
        side_frame_call_button->setIcon(icon5);
        side_frame_call_button->setIconSize(QSize(25, 25));

        horizontalLayout_9->addWidget(side_frame_call_button);


        horizontalLayout_7->addWidget(frame_7);

        search_frame = new QFrame(main_frame_header);
        search_frame->setObjectName(QStringLiteral("search_frame"));
        search_frame->setFrameShape(QFrame::StyledPanel);
        search_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_10 = new QHBoxLayout(search_frame);
        horizontalLayout_10->setObjectName(QStringLiteral("horizontalLayout_10"));
        searck_input = new QLineEdit(search_frame);
        searck_input->setObjectName(QStringLiteral("searck_input"));
        QFont font1;
        font1.setFamily(QStringLiteral("Roboto Medium"));
        searck_input->setFont(font1);
        searck_input->setStyleSheet(QLatin1String("border-radius:5;\n"
"background-color:rgb(255,255,255);\n"
""));

        horizontalLayout_10->addWidget(searck_input);

        download_button = new QPushButton(search_frame);
        download_button->setObjectName(QStringLiteral("download_button"));
        QIcon icon6;
        icon6.addFile(QStringLiteral("../resources/Icons/download.svg"), QSize(), QIcon::Normal, QIcon::Off);
        download_button->setIcon(icon6);
        download_button->setIconSize(QSize(25, 25));

        horizontalLayout_10->addWidget(download_button);

        login_button = new QPushButton(search_frame);
        login_button->setObjectName(QStringLiteral("login_button"));
        login_button->setIconSize(QSize(25, 25));

        horizontalLayout_10->addWidget(login_button);


        horizontalLayout_7->addWidget(search_frame);

        frame_5 = new QFrame(main_frame_header);
        frame_5->setObjectName(QStringLiteral("frame_5"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_8 = new QHBoxLayout(frame_5);
        horizontalLayout_8->setObjectName(QStringLiteral("horizontalLayout_8"));
        roll_down_button = new QPushButton(frame_5);
        roll_down_button->setObjectName(QStringLiteral("roll_down_button"));
        QIcon icon7;
        icon7.addFile(QStringLiteral("../resources/Icons/roll_down.svg"), QSize(), QIcon::Normal, QIcon::Off);
        roll_down_button->setIcon(icon7);
        roll_down_button->setIconSize(QSize(25, 25));

        horizontalLayout_8->addWidget(roll_down_button);

        expand_button = new QPushButton(frame_5);
        expand_button->setObjectName(QStringLiteral("expand_button"));
        QIcon icon8;
        icon8.addFile(QStringLiteral("../resources/Icons/expand.svg"), QSize(), QIcon::Normal, QIcon::Off);
        expand_button->setIcon(icon8);
        expand_button->setIconSize(QSize(25, 25));

        horizontalLayout_8->addWidget(expand_button);

        close_button = new QPushButton(frame_5);
        close_button->setObjectName(QStringLiteral("close_button"));
        QIcon icon9;
        icon9.addFile(QStringLiteral("../resources/Icons/close.svg"), QSize(), QIcon::Normal, QIcon::Off);
        close_button->setIcon(icon9);
        close_button->setIconSize(QSize(25, 25));

        horizontalLayout_8->addWidget(close_button);


        horizontalLayout_7->addWidget(frame_5);


        verticalLayout_3->addWidget(main_frame_header);

        main_frame_content = new QFrame(main_frame);
        main_frame_content->setObjectName(QStringLiteral("main_frame_content"));
        main_frame_content->setFrameShape(QFrame::StyledPanel);
        main_frame_content->setFrameShadow(QFrame::Raised);
        horizontalLayout_11 = new QHBoxLayout(main_frame_content);
        horizontalLayout_11->setSpacing(5);
        horizontalLayout_11->setObjectName(QStringLiteral("horizontalLayout_11"));
        horizontalLayout_11->setContentsMargins(5, 5, 5, 5);
        openGLWidget = new QOpenGLWidget(main_frame_content);
        openGLWidget->setObjectName(QStringLiteral("openGLWidget"));

        horizontalLayout_11->addWidget(openGLWidget);


        verticalLayout_3->addWidget(main_frame_content);

        main_frame_bottom = new QFrame(main_frame);
        main_frame_bottom->setObjectName(QStringLiteral("main_frame_bottom"));
        main_frame_bottom->setMaximumSize(QSize(16777215, 200));
        main_frame_bottom->setFrameShape(QFrame::StyledPanel);
        main_frame_bottom->setFrameShadow(QFrame::Raised);
        verticalLayout_4 = new QVBoxLayout(main_frame_bottom);
        verticalLayout_4->setSpacing(0);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        tools_frame = new QFrame(main_frame_bottom);
        tools_frame->setObjectName(QStringLiteral("tools_frame"));
        tools_frame->setMinimumSize(QSize(0, 0));
        tools_frame->setFrameShape(QFrame::StyledPanel);
        tools_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_9 = new QVBoxLayout(tools_frame);
        verticalLayout_9->setSpacing(0);
        verticalLayout_9->setObjectName(QStringLiteral("verticalLayout_9"));
        verticalLayout_9->setContentsMargins(0, 0, 0, 0);
        frame_3 = new QFrame(tools_frame);
        frame_3->setObjectName(QStringLiteral("frame_3"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        verticalLayout_10 = new QVBoxLayout(frame_3);
        verticalLayout_10->setObjectName(QStringLiteral("verticalLayout_10"));
        horizontalSlider = new QSlider(frame_3);
        horizontalSlider->setObjectName(QStringLiteral("horizontalSlider"));
        horizontalSlider->setOrientation(Qt::Horizontal);

        verticalLayout_10->addWidget(horizontalSlider);


        verticalLayout_9->addWidget(frame_3);

        scrollArea_2 = new QScrollArea(tools_frame);
        scrollArea_2->setObjectName(QStringLiteral("scrollArea_2"));
        scrollArea_2->setWidgetResizable(true);
        scrollAreaWidgetContents_3 = new QWidget();
        scrollAreaWidgetContents_3->setObjectName(QStringLiteral("scrollAreaWidgetContents_3"));
        scrollAreaWidgetContents_3->setGeometry(QRect(0, 0, 829, 263));
        verticalLayout_11 = new QVBoxLayout(scrollAreaWidgetContents_3);
        verticalLayout_11->setSpacing(10);
        verticalLayout_11->setObjectName(QStringLiteral("verticalLayout_11"));
        frame_8 = new QFrame(scrollAreaWidgetContents_3);
        frame_8->setObjectName(QStringLiteral("frame_8"));
        frame_8->setMinimumSize(QSize(0, 75));
        frame_8->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,150);"));
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);

        verticalLayout_11->addWidget(frame_8);

        frame_4 = new QFrame(scrollAreaWidgetContents_3);
        frame_4->setObjectName(QStringLiteral("frame_4"));
        frame_4->setMinimumSize(QSize(0, 75));
        frame_4->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,150);"));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);

        verticalLayout_11->addWidget(frame_4);

        frame_6 = new QFrame(scrollAreaWidgetContents_3);
        frame_6->setObjectName(QStringLiteral("frame_6"));
        frame_6->setMinimumSize(QSize(0, 75));
        frame_6->setStyleSheet(QLatin1String("border-radius: 16;\n"
"background-color: rgb(100,100,150);"));
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);

        verticalLayout_11->addWidget(frame_6);

        scrollArea_2->setWidget(scrollAreaWidgetContents_3);

        verticalLayout_9->addWidget(scrollArea_2);


        verticalLayout_4->addWidget(tools_frame);

        info_frame = new QFrame(main_frame_bottom);
        info_frame->setObjectName(QStringLiteral("info_frame"));
        info_frame->setMinimumSize(QSize(0, 30));
        info_frame->setMaximumSize(QSize(16777215, 30));
        info_frame->setFrameShape(QFrame::StyledPanel);
        info_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_13 = new QHBoxLayout(info_frame);
        horizontalLayout_13->setSpacing(0);
        horizontalLayout_13->setObjectName(QStringLiteral("horizontalLayout_13"));
        horizontalLayout_13->setContentsMargins(0, 0, 0, 0);
        video_name_frame = new QFrame(info_frame);
        video_name_frame->setObjectName(QStringLiteral("video_name_frame"));
        video_name_frame->setMinimumSize(QSize(200, 0));
        video_name_frame->setMaximumSize(QSize(200, 16777215));
        video_name_frame->setFrameShape(QFrame::StyledPanel);
        video_name_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(video_name_frame);
        verticalLayout_5->setSpacing(5);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        verticalLayout_5->setContentsMargins(5, 5, 5, 5);
        video_name = new QLabel(video_name_frame);
        video_name->setObjectName(QStringLiteral("video_name"));
        video_name->setCursor(QCursor(Qt::ArrowCursor));
        video_name->setFrameShape(QFrame::NoFrame);

        verticalLayout_5->addWidget(video_name);


        horizontalLayout_13->addWidget(video_name_frame);

        status_frame = new QFrame(info_frame);
        status_frame->setObjectName(QStringLiteral("status_frame"));
        status_frame->setMinimumSize(QSize(200, 0));
        status_frame->setMaximumSize(QSize(200, 16777215));
        status_frame->setFrameShape(QFrame::StyledPanel);
        status_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_6 = new QVBoxLayout(status_frame);
        verticalLayout_6->setSpacing(5);
        verticalLayout_6->setObjectName(QStringLiteral("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(5, 5, 5, 5);
        status = new QLabel(status_frame);
        status->setObjectName(QStringLiteral("status"));

        verticalLayout_6->addWidget(status);


        horizontalLayout_13->addWidget(status_frame);

        progress_bar_frame = new QFrame(info_frame);
        progress_bar_frame->setObjectName(QStringLiteral("progress_bar_frame"));
        progress_bar_frame->setFrameShape(QFrame::StyledPanel);
        progress_bar_frame->setFrameShadow(QFrame::Raised);
        verticalLayout_7 = new QVBoxLayout(progress_bar_frame);
        verticalLayout_7->setSpacing(0);
        verticalLayout_7->setObjectName(QStringLiteral("verticalLayout_7"));
        verticalLayout_7->setContentsMargins(0, 0, 0, 0);
        progressBar = new QProgressBar(progress_bar_frame);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        QFont font2;
        font2.setFamily(QStringLiteral("Roboto"));
        font2.setPointSize(8);
        font2.setBold(true);
        font2.setWeight(75);
        progressBar->setFont(font2);
        progressBar->setStyleSheet(QStringLiteral("text-color:white;"));
        progressBar->setValue(50);
        progressBar->setAlignment(Qt::AlignCenter);
        progressBar->setTextVisible(true);
        progressBar->setInvertedAppearance(false);

        verticalLayout_7->addWidget(progressBar);


        horizontalLayout_13->addWidget(progress_bar_frame);

        corner_holder = new QFrame(info_frame);
        corner_holder->setObjectName(QStringLiteral("corner_holder"));
        corner_holder->setMinimumSize(QSize(10, 10));
        corner_holder->setFrameShape(QFrame::StyledPanel);
        corner_holder->setFrameShadow(QFrame::Raised);

        horizontalLayout_13->addWidget(corner_holder, 0, Qt::AlignRight|Qt::AlignBottom);


        verticalLayout_4->addWidget(info_frame);


        verticalLayout_3->addWidget(main_frame_bottom);


        horizontalLayout->addWidget(main_frame);

        MainWindow->setCentralWidget(full_window_widget);

        retranslateUi(MainWindow);

        open_file_button->setDefault(false);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        pushButton->setText(QString());
        open_file_button->setText(QString());
        save_file_button->setText(QString());
        open_folder_button->setText(QString());
        select_folder_button->setText(QString());
        side_frame_call_button->setText(QString());
        searck_input->setText(QString());
        download_button->setText(QString());
        login_button->setText(QString());
        roll_down_button->setText(QString());
        expand_button->setText(QString());
        close_button->setText(QString());
        video_name->setText(QApplication::translate("MainWindow", "video_name", nullptr));
        status->setText(QApplication::translate("MainWindow", "video_status", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // FORMXDDIAM_H
