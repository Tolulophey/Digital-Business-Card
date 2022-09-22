import 'package:business_card/src/features/presentation/pages/authenticate/sign_in_page.dart';
import 'package:flutter/material.dart';
import 'package:page_transition/page_transition.dart';
import 'package:animated_splash_screen/animated_splash_screen.dart';


class SplashPage extends StatelessWidget {
  final bool showHome;
  const SplashPage({Key? key, required this.showHome}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AnimatedSplashScreen(
        splash: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset('assets/images/logo.svg'),
            ],
          ),
        ),
        backgroundColor: Color(0xFF800080),
        splashTransition: SplashTransition.scaleTransition,
        pageTransitionType: PageTransitionType.leftToRight,
        splashIconSize: 390,
        nextScreen: showHome ? const SignInPage());
  }
}


/*
AnimatedSplashScreen(
duration: 3000,
splash: Center(
child: Column(
mainAxisAlignment: MainAxisAlignment.center,
children: [
Image.asset('assets/images/logo.svg')
],
),
),
backgroundColor: Color(0xFF800080),
splashTransition: SplashTransition.scaleTransition,
pageTransitionType: PageTransitionType.leftToRight,
splashIconSize: 390,
nextScreen: showHome ? const SignInPage()
);*/
