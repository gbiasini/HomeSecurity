﻿using Android.App;
using Android.Widget;
using HomeSecurityApp.Droid.Dependecy;
using HomeSecurityApp.Utility.Interface;

[assembly: Xamarin.Forms.Dependency(typeof(MessageAndroid))]
namespace HomeSecurityApp.Droid.Dependecy
{
    public class MessageAndroid : IMessage
    {
        public void LongAlert(string message)
        {
            Toast.MakeText(Application.Context, message, ToastLength.Long).Show();
        }

        public void ShortAlert(string message)
        {
            Toast.MakeText(Application.Context, message, ToastLength.Short).Show();
        }
    }
}