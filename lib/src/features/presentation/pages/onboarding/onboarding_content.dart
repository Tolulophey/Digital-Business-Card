import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';


class OnboardingContent extends StatelessWidget {
  final String imageSrc, description;
  final int? dataLength;
  final double? currentIndex;
  const OnboardingContent(
      {Key? key,
      required this.imageSrc,
      required this.description,
      this.dataLength,
      this.currentIndex})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              SvgPicture.asset(
                  imageSrc
              ),
              const SizedBox(height: 40),
              Padding(
                  padding: EdgeInsets.symmetric(horizontal: 50),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                        description,
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                       fontSize: 12,
                        color: Color(0xFFFFFFFF),
                        letterSpacing: 1,
                        wordSpacing: 1.5
                      ),
                    )
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
