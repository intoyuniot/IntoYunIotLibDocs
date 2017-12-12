/** @file
 * This is a sample Arduino library showing how to use IntoYunIotLibDocs.
 *
 * Copyright (c) 2015 - Present MOLMC
 * This software is released under the MIT license. See the attached LICENSE file for details.
 */
#ifndef INTOYUNIOTLIBDOCS_h
#define INTOYUNIOTLIBDOCS_h

#include <Arduino.h>

/**
 * Brief description of the IntoYunIotLibDocs class.
 *
 * Detailed description of the IntoYunIotLibDocs class.
 */
class IntoYunIotLibDocs
{
  public:
    /**
     * Constructor.
     *
     * Detailed constructor description.
     */
    IntoYunIotLibDocs();

    /**
     * Brief documentation for method1().
     *
     * Detailed documentation for method1().
     */
    void method1();

    /**
     * Brief documentation for method2().
     *
     * Detailed documentation for method2().
     *
     * @param p1  method2()'s first parameter.
     * @param p2  method2()'s second parameter.
     * @return    return value for method2().
     */
    int method2(int p1, int p2);

  private:
    int member1;
    float member2;

    int method3(int p1);
};

#endif
