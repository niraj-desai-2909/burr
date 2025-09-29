/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/**
 * Simple loading component
 */
export const Loading = () => {
  return (
    <div className="flex items-center justify-center space-x-2 w-full h-full">
      <div className="w-8 h-8 bg-dwred/50 rounded-full animate-pulse animation-delay-0"></div>
      <div className="w-8 h-8 bg-dwdarkblue/50 rounded-full animate-pulse animation-delay-500"></div>
      <div className="w-8 h-8 bg-dwlightblue/50 rounded-full animate-pulse animation-delay-1000"></div>
    </div>
  );
};
